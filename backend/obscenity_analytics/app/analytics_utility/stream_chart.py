from datetime import datetime, timedelta
from ..database.database import NSFW


async def get_stream_chart_data():
    end_date = datetime.now()
    start_date = end_date - timedelta(days=60)
    stream_chart_data = []
    pipeline = [
        {"$match": {"date_of_acquisition": {"$gte": start_date, "$lte": end_date}}},
        {
            "$group": {
                "_id": {
                    "$dateToString": {
                        "format": "%Y-%m-%d",
                        "date": "$date_of_acquisition",
                    }
                },
                "nsfw_count": {"$sum": {"$cond": [{"$eq": ["$result", "NSFW"]}, 1, 0]}},
                "sfw_count": {"$sum": {"$cond": [{"$eq": ["$result", "SFW"]}, 1, 0]}},
            }
        },
        {"$sort": {"_id": 1}},
    ]

    result = list(NSFW.aggregate(pipeline))
    for entry in result:
        stream_chart_data.append(
            {"nsfw": entry["nsfw_count"], "sfw": entry["sfw_count"]}
        )

    return stream_chart_data


# Sample output
# [
#   {"nsfw": 176, "sfw": 185},
#   {"nsfw": 29, "sfw": 140},
#   {"nsfw": 172, "sfw": 88},
#   {"nsfw": 46, "sfw": 155},
#   {"nsfw": 22, "sfw": 55},
#   {"nsfw": 12, "sfw": 133},
#   {"nsfw": 132, "sfw": 85},
#   {"nsfw": 11, "sfw": 49},
#   {"nsfw": 56, "sfw": 95}
# ]
