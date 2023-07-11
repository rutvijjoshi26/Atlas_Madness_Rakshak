from fastapi import APIRouter,Request
from ...utility.utils import process_image_files
from ..models.nsfw import ImageUrls

import time



router=APIRouter()

@router.post("/api/nsfw/image")
async def predict_image_nsfw(urls:ImageUrls,request:Request):
    client_host=request.client.host
    start_time=time.time()
    [results,unprocessed_images]=await process_image_files(urls.urls,client_host)
    end_time=time.time()
    print(f'Time needed : {end_time-start_time}')
    return {"result":results,"unprocessed_images":unprocessed_images}