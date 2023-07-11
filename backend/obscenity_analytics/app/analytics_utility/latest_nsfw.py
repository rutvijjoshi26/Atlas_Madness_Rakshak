from ..database.database import NSFW
from fastapi import HTTPException, status


async def get_latest_nsfw():
    try:
        pipeline = [
            {"$match": {"result": "NSFW"}},
            {"$sort": {"date_of_acquisition": -1}},
            {
                "$project": {
                    "_id": 0,
                    "counter": 1,
                    "result": 1,
                    "date_of_acquisition": {
                        "$dateToString": {
                            "format": "%Y-%m-%d %H:%M:%S",
                            "date": "$date_of_acquisition",
                        }
                    },
                }
            },
        ]
        result = list(NSFW.aggregate(pipeline))
        return result[:4]

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)
        )
