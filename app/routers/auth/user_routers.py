from fastapi import APIRouter
from app.utils.users_methods import get_all_users, create_user, delete_user_by_id
from app.db.session import SesionDep, setup_database
from app.db.models import UserModel
from app.schemas.user import UserCreate, UserOut
from async_lru import alru_cache

router = APIRouter(tags=['auth'])

ttl_cache = 120

@router.get("/users", summary="Получить всех пользователей")
@alru_cache(ttl=ttl_cache)
async def get_all_users_router(session: SesionDep) -> list[UserCreate]:
    users = await get_all_users(session)
    return users


@router.post("/users/create/", summary="Создать пользователя")
async def create_user_router(data: UserCreate, session: SesionDep) -> dict[str, str]:
    user = await create_user(data, session)
    return user


@router.delete("/users/delete/{user_id}", summary="Удалить пользователя")
async def delete_user_router(user_id: int, session: SesionDep) -> UserCreate:
    user = await delete_user_by_id(user_id, session)
    return user


@router.post("/setup_database", summary="Перезагрузить базу данных")
async def post_setup_database() -> dict[str, str]:
    data = await setup_database()
    return data
