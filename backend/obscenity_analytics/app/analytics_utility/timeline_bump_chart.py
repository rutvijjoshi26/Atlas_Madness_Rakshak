from datetime import datetime, timedelta
from ..database.database import NSFW


async def get_timeline_bump_chart():
    end_date = datetime.now()
    start_date = end_date - timedelta(days=30)
    file_types = ["image", "text", "video"]
    chart_data = []
    for file_type in file_types:
        nsfw_pipeline = [
            {
                "$match": {
                    "result": "NSFW",
                    "type_of_file": file_type,
                    "date_of_acquisition": {"$gte": start_date, "$lte": end_date},
                },
            },
            {
                "$group": {
                    "_id": {
                        "$dateToString": {
                            "format": "%Y-%m-%d",
                            "date": "$date_of_acquisition",
                        },
                    },
                    "count": {"$sum": 1},
                },
            },
            {
                "$project": {
                    "x": "$_id",
                    "y": "$count",
                },
            },
        ]

        sfw_pipeline = [
            {
                "$match": {
                    "result": "SFW",
                    "type_of_file": file_type,
                    "date_of_acquisition": {"$gte": start_date, "$lte": end_date},
                },
            },
            {
                "$group": {
                    "_id": {
                        "$dateToString": {
                            "format": "%Y-%m-%d",
                            "date": "$date_of_acquisition",
                        },
                    },
                    "count": {"$sum": 1},
                },
            },
            {
                "$project": {
                    "x": "$_id",
                    "y": "$count",
                },
            },
        ]

        nsfw_result = list(NSFW.aggregate(nsfw_pipeline))
        sfw_result = list(NSFW.aggregate(sfw_pipeline))

        nsfw_data = [{"x": item["x"], "y": item["y"]} for item in nsfw_result]
        sfw_data = [{"x": item["x"], "y": item["y"]} for item in sfw_result]

        file_data = {
            "id": file_type,
            "data": [
                {"id": "NSFW", "data": nsfw_data},
                {"id": "SFW", "data": sfw_data}
            ]
        }

        chart_data.append(file_data)
    return chart_data
