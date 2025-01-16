from fastapi import APIRouter
from app.utils.get_github_data import get_notifications
from async_lru import alru_cache

router = APIRouter(tags=["github"], prefix='/github')


@router.get("/notifications")
@alru_cache(ttl=120)
async def get_notifications_from_github():
    notifications = await get_notifications(2)
    return notifications
