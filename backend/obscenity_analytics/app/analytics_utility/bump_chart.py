from datetime import datetime, timedelta
from ..database.database import NSFW


async def get_bump_chart_data():
    end_date = datetime.now()
    start_date = end_date - timedelta(days=30)
    file_types = ["image", "text", "video"]
    chart_data = []
    for file_type in file_types:
        pipeline = [
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
                    "x": {"$dateFromString": {"dateString": "$_id"}},
                    "y": "$count",
                },
            },
        ]

        result = list(NSFW.aggregate(pipeline))

        data = [{"x": item["x"], "y": item["y"]} for item in result]

        chart_data.append({"id": file_type, "data": data})

    return chart_data


# This is the sample output of above code
# [
#   {
#     "id": "Image",
#     "data": [
#       {"x": "2023-05-22", "y": 10},
#       {"x": "2023-05-23", "y": 8},
#       {"x": "2023-05-24", "y": 12},
#       ...
#     ]
#   },
#   {
#     "id": "Text",
#     "data": [
#       {"x": "2023-05-22", "y": 5},
#       {"x": "2023-05-23", "y": 7},
#       {"x": "2023-05-24", "y": 3},
#       ...
#     ]
#   },
#   {
#     "id": "Video",
#     "data": [
#       {"x": "2023-05-22", "y": 15},
#       {"x": "2023-05-23", "y": 13},
#       {"x": "2023-05-24", "y": 10},
#       ...
#     ]
#   }
# ]
