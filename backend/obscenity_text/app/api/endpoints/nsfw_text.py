from fastapi import APIRouter,Request
from ...utility.obscenity_text import process_text_obscenity

import time

router=APIRouter()

@router.post("/api/nsfw/text")
async def predict_text_nsfw(text:str,request:Request):
    client_host=request.client.host
    start_time=time.time()
    result=await process_text_obscenity(text,client_host)
    end_time=time.time()
    print(f'Time needed : {end_time-start_time}')
    return {"results":result}