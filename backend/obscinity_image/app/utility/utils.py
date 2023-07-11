import os
import aiohttp
import asyncio
from datetime import datetime

from ..utility.obscenity_image import predict_one_tflite
from ..schemas.nsfw import FileMetadata
from ..database.connection import obscenity_collection


async def remove_file(filepath: str):
    try:
        os.remove(filepath)
        print(f"File {filepath} has been removed.")
    except OSError as error:
        print(f"Error deleting file {filepath}: {error}")


def find_majority_label(labels):
    count = 0
    majority_label = None

    for label in labels:
        if count == 0:
            majority_label = label
            count = 1
        elif label == majority_label:
            count += 1
        else:
            count -= 1

    return majority_label


async def download_file(url, filename):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                print(f"Response status code: {response.status}")
                if response.status == 200:
                    with open(filename, "wb") as f:
                        while True:
                            chunk = await response.content.read(1024)
                            if not chunk:
                                break
                            f.write(chunk)
                    print(f"Downloaded {filename}")
                else:
                    print(f"Failed to download {filename}")
    except aiohttp.ClientError as e:
        print(f"Error downloading file: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


async def process_image(file_location):
    result = await predict_one_tflite(file_location)
    return result


async def process_image_files(urls, client_host):
    unprocessed_images = 0
    tasks = []
    for i, url in enumerate(urls):
        filename = f"/tmp/image_{i}.jpg"
        print(f"Downloading {url} to {filename}...")
        task = asyncio.create_task(download_file(url, filename))
        tasks.append(task)
    await asyncio.gather(*tasks)

    results = []

    for i in range(len(urls)):
        filename = f"/tmp/image_{i}.jpg"
        print(f"Processing {filename}...")
        result = await process_image(filename)
        if result == None:
            unprocessed_images += 1
            continue
        else:
            try:
                file_metadata = FileMetadata(
                    link=urls[i],
                    size=os.path.getsize(filename),
                    date_of_acquisition=datetime.now(),
                    source=client_host,
                    result=result,
                    type_of_file="image",
                )
                query = {"link": urls[i]}
                update = {"$inc": {"counter": 1}}
                result_of_updation = obscenity_collection.update_one(query, update)
                if result_of_updation.modified_count == 0:
                    obscenity_collection.insert_one(file_metadata.dict())
                    print("Entry in database made")
                else:
                    print("Counter Increased for existing Entry")
            except Exception as e:
                print(f"Error occurred while interacting with the database: {str(e)}")

            results.append(result)

    tasks = []
    for i in range(len(urls)):
        filename = f"/tmp/image_{i}.jpg"
        print(f"Removing {filename}...")
        task = asyncio.create_task(remove_file(filename))
        tasks.append(task)
    await asyncio.gather(*tasks)

    majority_label = find_majority_label(results)
    return [majority_label, unprocessed_images]
