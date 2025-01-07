from fastapi import APIRouter
from app.utils.users_methods import get_all_users, create_user, delete_user_by_id

router = APIRouter()


@router.get("/users")
async def get_all_users_router():
    users = await get_all_users()
    return users


@router.post("/users/create/")
async def create_user_router(username: str, email: str, password: str):
    user = await create_user(username, email, password)
    return user


@router.delete("/users/delete/{user_id}")
async def delete_user_router(user_id: int):
    user = await delete_user_by_id(user_id)
    return user
