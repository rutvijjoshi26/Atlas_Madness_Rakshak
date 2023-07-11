from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.endpoints import nsfw_text

from app.database.connection import client

app=FastAPI()

origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.get("/")
def main_text():
    return {"message": "Test"}

app.include_router(nsfw_text.router)

@app.on_event("shutdown")
async def shutdown_event():
    client.close()

