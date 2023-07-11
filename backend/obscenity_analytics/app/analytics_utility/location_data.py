from ..database.database import NSFW
from fastapi import HTTPException, status
from ip2geotools.databases.noncommercial import DbIpCity


async def get_location_data():
    try:
        results = NSFW.find({"results": "NSFW"}, {"_id": 0, "source": 1})
        location_data = []

        for result in results:
            ip = result["source"]
            location = get_ip_location(ip)

            location_data.append(
                {
                    "id": location["id"],
                    "coordinates": location["coordinates"],
                    "state": location["state"],
                }
            )

        return location_data

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e),
        )


def get_ip_location(ip):
    try:
        response = DbIpCity.get(ip, api_key="free")

        latitude = response.latitude
        longitude = response.longitude
        state = response.region

        location = {
            "id": None,
            "coordinates": [latitude, longitude],
            "state": state,
        }

        return location

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e),
        )
