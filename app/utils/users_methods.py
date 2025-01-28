from asyncio import run
from typing import Sequence

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.db.models import User
from app.db.session import connection
from app.dependencies import list_of_admins


@connection
async def create_user(username: str, email: str, password: str, session: AsyncSession) -> User:
    """
    Создает нового пользователя с использованием ORM SQLAlchemy.

    Аргументы:
    - username: str - имя пользователя
    - email: str - адрес электронной почты
    - password: str - пароль пользователя
    - session: AsyncSession - асинхронная сессия базы данных
    - admin: bool - является ли пользователь администратором
    """
    if await session.scalar(select(User).where(User.username == username)):
        return {'error': 'Пользователь с таким именем уже существует'}
    admin = False
    if username in list_of_admins:
        admin = True
    user = User(username=username, email=email, password=password, admin=admin)
    session.add(user)
    await session.commit()
    return user


@connection
async def delete_user_by_id(id: int, session: AsyncSession) -> None:
    """
    Удаляет пользователя из базы данных по его идентификатору

    :param id: int - идентификатор пользователя
    :param session: AsyncSession - асинхронная сессия базы данных
    :return: None
    """
    if not await session.scalar(select(User).where(User.id == id)):
        return {'error': 'Пользователь не найден'}
    obj = await session.get(User, id)

    await session.delete(obj)
    await session.commit()
    return obj


@connection
async def get_all_users(session: AsyncSession) -> list[dict[str, bool | str]]:
    """
    Возвращает всех пользователей из базы данных

    :param session: AsyncSession
    :return: None
    """
    # Создаем запрос для выборки всех пользователей
    query = select(User)

    # Выполняем запрос и получаем результат
    result = await session.execute(query)

    # Извлекаем записи как объекты модели
    records = result.scalars().all()
    result = [{'username': i.username, 'password': i.password, 'email': i.email, 'admin': i.admin} for i in records]

    # Возвращаем список всех пользователей
    return result
