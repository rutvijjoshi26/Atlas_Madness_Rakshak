from fastapi import HTTPException, status
from ..database.database import NSFW


async def get_trending_nsfw():
    try:
        pipeline = [
            {"$match": {"result": "NSFW", "counter": {"$exists": True}}},
            {"$sort": {"counter": -1}},
            {"$project": {"_id": 0, "counter": 1, "result": 1}},
        ]
        result = list(NSFW.aggregate(pipeline))
        return result[:4]

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)
        )
