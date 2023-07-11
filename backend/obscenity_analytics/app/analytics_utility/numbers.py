from ..database.database import NSFW
from datetime import datetime, timedelta
from fastapi import HTTPException, status


async def get_numbers():
    try:
        # Total Number of files
        total_files = NSFW.count_documents({})

        # NSFW Detection rate
        nsfw_files = NSFW.count_documents({"result": "NSFW"})
        nsfw_detection_rate = nsfw_files / total_files

        # NSFW/SFW Ratio
        sfw_files = total_files - nsfw_files
        nsfw_sfw_ratio = nsfw_files / sfw_files
        

        end_date = datetime.now()
        start_date = end_date - timedelta(days=30)
        last_30_days_nsfw_files = len(
            list(
                NSFW.find(
                    {
                        "result": "NSFW",
                        "date_of_acquisition": {
                            "$gte": start_date,
                            "$lte": end_date,
                        },
                    }
                )
            )
        )

        today_nsfw_files = len(
            list(
                NSFW.find(
                    {
                        "result": "NSFW",
                        "date_of_acquisition": {
                            "$gte": end_date - timedelta(days=1),
                            "$lte": end_date,
                        },
                    }
                )
            )
        )

        # Percentage Increase in NSFW files
        if today_nsfw_files != 0:
            percentage_increase = (
                (today_nsfw_files - last_30_days_nsfw_files) / last_30_days_nsfw_files
            ) * 100
        else:
            percentage_increase=0

        return {
            "Total files": total_files,
            "NSFW Detection Rate": round(nsfw_detection_rate,2),
            "NSFW/SFW": round(nsfw_sfw_ratio,2),
            "NSFW Percentage Increase": percentage_increase,
        }

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)
        )
