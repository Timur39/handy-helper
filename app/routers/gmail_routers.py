from fastapi import APIRouter
from app.utils.get_gmail_data import get_gmails
from async_lru import alru_cache

router = APIRouter(tags=["gmail"], prefix='/gmail')


@router.get("/emails")
@alru_cache(ttl=120)
async def get_emails_from_gmail():
    emails = await get_gmails(10)
    return emails
