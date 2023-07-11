from fastapi import APIRouter
from ..analytics_utility.numbers import get_numbers
from ..analytics_utility.bump_chart import get_bump_chart_data
from ..analytics_utility.stream_chart import get_stream_chart_data
from ..analytics_utility.trending_nsfw import get_trending_nsfw
from ..analytics_utility.latest_nsfw import get_latest_nsfw
from ..analytics_utility.timeline_numbers import get_timeline_numbers
from ..analytics_utility.timeline_calender import get_timeline_calendar
from ..analytics_utility.location_data import get_location_data
from ..analytics_utility.timeline_bump_chart import get_timeline_bump_chart
from ..database.database import NSFW


router = APIRouter()


@router.get("/overview/numbers")
async def get_overview_numbers():
    result = await get_numbers()
    return result


@router.get("/overview/bump_chart")
async def get_area_bump_chart_data():
    result = await get_bump_chart_data()
    return result


@router.get("/overview/stream_chart")
async def get_stream_main_chart_data():
    result = await get_stream_chart_data()
    return result


@router.get("/details")
async def get_all_entries():
    entries = list(NSFW.find())
    for entry in entries:
        entry["_id"] = str(entry["_id"])
    return entries


@router.get("/overview/trending")
async def get_trending_nsfw_main():
    result = await get_trending_nsfw()
    return result


@router.get("/overview/alerts")
async def get_alerts_nsfw():
    result = await get_latest_nsfw()
    return result


@router.get("/timeline/numbers")
async def get_timeline_numbers_main():
    result = await get_timeline_numbers()
    return result


@router.get("/timeline/calender")
async def get_timeline_calender_main():
    result = await get_timeline_calendar()
    return result


@router.get("/timeline/bump_chart")
async def get_timeline_bump_chart_main():
    result = await get_timeline_bump_chart()
    return result

@router.get("/mapview/map_details")
async def get_map_view_details_main():
    result=await get_location_data()
    return result
