from fastapi import APIRouter
from app.utils.get_modrinth_data import get_notifications
from async_lru import alru_cache

router = APIRouter(tags=["modrinth"], prefix='/modrinth')


@router.get("/notifications")
@alru_cache(ttl=120)
async def get_notifications_from_modrinth():
    notifications = await get_notifications(5)
    return notifications
