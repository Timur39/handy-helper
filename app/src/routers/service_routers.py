from fastapi import APIRouter, Depends
from src.utils.api_methods.get_github_data import get_github_notifications
from src.utils.api_methods.get_gmail_data import get_gmails
from src.utils.api_methods.get_news_data import get_all_news
from src.utils.api_methods.get_modrinth_data import get_modrinth_notifications
from src.utils.api_methods.get_quotes import get_currencies_price
from src.utils.api_methods.get_stepik_data import get_user_activity
from src.utils.api_methods.get_todoist_data import get_today_tasks
from src.utils.api_methods.get_youtube_data import get_youtube_videos
from async_lru import alru_cache
from src.schemas.services import Github_Schema, News_Schema, Price_Schema, Gmail_Schema, \
                                    Todoist_Schema, Modrinth_Schema, Stepik_Schema, Youtube_Schema
router = APIRouter(tags=["api"], prefix='/api')
ttl_cache = 3600

@router.get("/github_notifications", summary="Получить уведомления из GitHub", 
            description="Получить уведомления из GitHub за последние 2 дня")
@alru_cache(ttl=ttl_cache)
async def get_notifications_from_github() -> list[Github_Schema] | None:
    notifications = await get_github_notifications(2)
    return notifications


@router.get("/emails", summary="Получить сообщения из Gmail",
            description="Получить последние 10 сообщений из Gmail")
@alru_cache(ttl=ttl_cache)
async def get_emails_from_gmail() -> list[Gmail_Schema] | None:
    emails = await get_gmails(10)
    return emails

@router.get("/modrinth_notifications", summary="Получить уведомления из Modrinth",
            description="Получить последние 5 уведомлений из Modrinth")
@alru_cache(ttl=ttl_cache)
async def get_notifications_from_modrinth() -> list[Modrinth_Schema]:
    notifications = await get_modrinth_notifications(5)
    return notifications

@router.get("/news", summary="Получить новости", 
            description="Получить последние 20 сообщений со всех источников")
@alru_cache(ttl=ttl_cache)
async def get_news() -> list[News_Schema]:
    news = await get_all_news()
    return news

@router.get("/prices", summary="Получить курсы валют", 
            description="Получить курсы валют. Рубля, доллара, биткойна")
@alru_cache(ttl=ttl_cache)
async def get_prices() -> list[Price_Schema] | None:
    prices = await get_currencies_price()
    return prices

@router.get("/stepik_user_activity", summary="Получить статистику Stepik",
            description="Получить статистику Stepik. Сделанные задачи, полученные сертификаты")
@alru_cache(ttl=ttl_cache)
async def get_stepik_activity() -> list[Stepik_Schema]:
    user_activity = await get_user_activity()
    return user_activity

@router.get("/todoist_tasks", summary="Получить задачи из Todoist",
            description="Получить задачи на сегодня из Todoist")
@alru_cache(ttl=ttl_cache)
async def get_todoist_tasks() -> list[Todoist_Schema]:
    tasks = await get_today_tasks()
    return tasks

@router.get("/youtube_videos", summary="Получить видео из Youtube",
            description="Получить видео за последние 24 часа из Youtube. С определенных каналов")
@alru_cache(ttl=ttl_cache)
async def get_youtube() -> list[Youtube_Schema]:
    video = await get_youtube_videos()
    return video
