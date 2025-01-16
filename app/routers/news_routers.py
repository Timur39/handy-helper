from fastapi import APIRouter
from app.utils.get_news_data import main
from async_lru import alru_cache

router = APIRouter(tags=["news"], prefix='/news')


@router.get("/news")
@alru_cache(ttl=120)
async def get_news():
    news = await main()
    return news
