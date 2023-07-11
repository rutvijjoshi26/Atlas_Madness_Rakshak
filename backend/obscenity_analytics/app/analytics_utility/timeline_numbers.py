from ..database.database import NSFW
from datetime import datetime, timedelta
from fastapi import HTTPException, status


async def get_timeline_numbers():
    try:
        file_types = ["text", "image", "video"]
        counts = []
        for file_type in file_types:
            counts.append(
                {
                    "file_type": file_type,
                    "total_files": NSFW.count_documents({"type_of_file": file_type}),
                }
            )
        averages = []
        growth_rates = []

        for file_type in file_types:
            pipeline = [
                {"$match": {"type_of_file": file_type}},
                {
                    "$group": {
                        "_id": {
                            "$dateToString": {
                                "format": "%Y-%m-%d",
                                "date": "$date_of_acquisition",
                            }
                        },
                        "count": {"$sum": 1},
                    }
                },
                {"$group": {"_id": None, "average_files_per_day": {"$avg": "$count"}}},
            ]
            result = list(NSFW.aggregate(pipeline))

            if not result:
                average_files_per_day = 0
            else:
                average_files_per_day = result[0]["average_files_per_day"]
            averages.append(
                {"file_type": file_type, "average_files_per_day": average_files_per_day}
            )

            previous_date = datetime.now() - timedelta(days=30)
            previous_files = NSFW.count_documents(
                {
                    "type_of_file": file_type,
                    "date_of_acquisition": {"$lt": previous_date},
                }
            )
            # print(previous_files)
            current_date = datetime.now()
            current_files = NSFW.count_documents(
                {
                    "type_of_file": file_type,
                    "date_of_acquisition": {"$gte": previous_date, "$lt": current_date},
                }
            )
            # print(current_files)
            if previous_files != 0:
                growth_rate = ((current_files - previous_files) / previous_files) * 100
                growth_rates.append(
                    {"type_of_file": file_type, "growth_rate": growth_rate}
                )
            else:
                growth_rates.append({"type_of_file": file_type, "growth_rate": 0})

        return {"counts": counts, "averages": averages, "growth_rates": growth_rates}

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred while retrieving timeline numbers.",
        ) from e
