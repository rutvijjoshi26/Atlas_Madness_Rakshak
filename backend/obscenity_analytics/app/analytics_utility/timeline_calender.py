from datetime import datetime, timedelta
from ..database.database import NSFW
from fastapi import HTTPException, status


async def get_timeline_calendar():
    end_date = datetime.now()
    start_date = end_date - timedelta(days=120)
    file_types = ["text", "image", "video"]
    calendar_data = []

    for file_type in file_types:
        pipeline = [
            {
                "$match": {
                    "result": "NSFW",
                    "type_of_file": file_type,
                    "date_of_acquisition": {"$gte": start_date, "$lte": end_date},
                }
            },
            {
                "$group": {
                    "_id": {
                        "$dateToString": {
                            "format": "%Y-%m-%d",
                            "date": "$date_of_acquisition",
                        }
                    },
                    "value": {"$sum": 1},
                }
            },
            {"$project": {"day": "$_id", "value": "$value"}},
        ]

        try:
            result = list(NSFW.aggregate(pipeline))
            file_data = [
                {"day": item["day"][:10], "value": item["value"]} for item in result
            ]
            calendar_data.append({"file_type": file_type, "data": file_data})

        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)
            )

    return calendar_data
