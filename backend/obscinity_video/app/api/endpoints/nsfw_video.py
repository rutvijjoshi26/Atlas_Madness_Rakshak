from fastapi import APIRouter,Request
from ...utility.utils import process_video_files
from ..models.nsfw_models import VideoUrls

import time

router=APIRouter()

@router.post("/api/nsfw/video")
async def predict_video_nsfw(urls:VideoUrls,request:Request):
    client_host=request.client.host
    start_time=time.time()
    [results]=await process_video_files(urls.urls,client_host)
    end_time=time.time()
    print(f'Time needed : {end_time-start_time}')
    return {"result":results}