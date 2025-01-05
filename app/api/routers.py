from fastapi import APIRouter

router = APIRouter()


@router.get("/users/")
async def get_users():
    return [{"name": "John Doe", 'email': "john@example.com"}]

