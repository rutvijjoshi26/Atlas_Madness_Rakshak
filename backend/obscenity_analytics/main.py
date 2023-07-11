from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.router.analytics import router as analytics_router
from app.config import settings
from app.database.database import client


app = FastAPI()

origins = [
    settings.CLIENT_ORIGIN,
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(analytics_router,tags=['Analytics'],prefix="/api/analytics")


@app.get("/api/")
def root():
    return {"message": "Test"}

@app.on_event("shutdown")
async def shutdown_event():
    client.close()

