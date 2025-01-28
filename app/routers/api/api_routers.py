from fastapi import APIRouter
from app.utils.api_methods.get_github_data import get_github_notifications
from app.utils.api_methods.get_gmail_data import get_gmails
from app.utils.api_methods.get_news_data import get_all_news
from app.utils.api_methods.get_modrinth_data import get_modrinth_notifications
from app.utils.api_methods.get_quotes import get_currencies_price
from app.utils.api_methods.get_stepik_data import get_user_activity
from app.utils.api_methods.get_todoist_data import get_today_tasks
from app.utils.api_methods.get_youtube_data import get_youtube_videos
from async_lru import alru_cache

router = APIRouter(tags=["api"], prefix='/api')
ttl_cache = 120

@router.get("/github_notifications")
@alru_cache(ttl=ttl_cache)
async def get_notifications_from_github():
    notifications = await get_github_notifications(2)
    return notifications

@router.get("/emails")
@alru_cache(ttl=ttl_cache)
async def get_emails_from_gmail():
    emails = await get_gmails(10)
    return emails

@router.get("/modrinth_notifications")
@alru_cache(ttl=ttl_cache)
async def get_notifications_from_modrinth():
    notifications = await get_modrinth_notifications(5)
    return notifications

@router.get("/news")
@alru_cache(ttl=ttl_cache)
async def get_news():
    news = await get_all_news()
    return news

@router.get("/prices")
@alru_cache(ttl=ttl_cache)
async def get_prices():
    prices = await get_currencies_price()
    return prices

@router.get("/stepik_user_activity")
@alru_cache(ttl=ttl_cache)
async def get_tasks():
    user_activity = await get_user_activity()
    return user_activity

@router.get("/todoist_tasks")
@alru_cache(ttl=ttl_cache)
async def get_tasks():
    tasks = await get_today_tasks()
    return tasks

@router.get("/youtube_videos")
@alru_cache(ttl=1200)
async def get_youtube():
    video = await get_youtube_videos()
    return video
