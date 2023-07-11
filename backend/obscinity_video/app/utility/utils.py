import os
import aiohttp
import asyncio
from datetime import datetime

from ..utility.obscenity_video import multiprocess
from ..schema.nsfw import FileMetadata
from ..database.connection import obscenity_collection


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

async def remove_file(filepath: str):
    os.remove(filepath)



async def download_file(url, filename):
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


async def process_video(file_location):
    await asyncio.sleep(0)
    # result=await loop.run_until_complete(multiprocess(file_location))
    result = await multiprocess(file_location)
    return result


async def process_video_files(urls, client_host):
    unprocessed_videos = 0
    tasks = []
    downloaded_files = []
    for i, url in enumerate(urls):
        filename = f"/tmp/video_{i}.mp4"
        print(f"Downloading {url} to {filename}...")
        task = asyncio.create_task(download_file(url, filename))
        tasks.append(task)
    await asyncio.gather(*tasks)

    results = []
    for i, url in enumerate(urls):
        filename = f"/tmp/video_{i}.mp4"
        if os.path.exists(filename):
            print(f"Processing file : {filename}")
            result = await process_video(filename)
            if result == None:
                unprocessed_videos += 1
                continue
            else:
                try:
                    filemetadata = FileMetadata(
                        link=urls[i],
                        size=os.path.getsize(filename),
                        date_of_acquisition=datetime.now(),
                        source=client_host,
                        result=result,
                        type_of_file="video",
                    )
                    query = {"link": urls[i]}
                    update = {"$inc": {"counter": 1}}
                    result_of_updation = obscenity_collection.update_one(query, update)
                    if result_of_updation.modified_count == 0:
                        obscenity_collection.insert_one(filemetadata.dict())
                        print("Entry in databse made")
                    else:
                        print("Counter increased")
                except Exception as e:
                    print(
                        f"Error occurred while interacting with the database: {str(e)}"
                    )
                results.append(result)
            downloaded_files.append(filename)

    tasks = []
    for i, url in enumerate(urls):
        filename = f"/tmp/video_{i}.mp4"
        if os.path.exists(filename):
            print(f"Removing {filename}...")
            task = asyncio.create_task(remove_file(filename))
            tasks.append(task)
    await asyncio.gather(*tasks)

    majority_label = find_majority_label(results)
    return [majority_label]
