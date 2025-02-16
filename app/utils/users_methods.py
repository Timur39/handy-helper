from app.db.session import SesionDep
from sqlalchemy import select

from app.db.models import UserModel
from app.schemas.user import UserCreate, UserOut
from app.dependencies import list_of_admins


async def create_user(data: UserCreate, session: SesionDep) -> UserModel:
    """
    Создает нового пользователя

    :param session: SesionDep
    :param data: UserCreate
    :return: User
    """
    if await session.scalar(select(UserModel).where(UserModel.username == data.username)):
        return {'error': 'Пользователь с таким именем уже существует'}
    
    admin = False
    if data.username in list_of_admins:
        admin = True

    user = UserModel(username=data.username, 
                email=data.email, 
                password=data.password, 
                admin=admin)
    
    session.add(user)

    await session.commit()

    return {'status': 'Пользователь успешно создан'}


async def delete_user_by_id(data: UserOut, session: SesionDep) -> UserModel | None:
    """
    Удаляет пользователя из базы данных по его идентификатору

    :param id: int
    :param session: SesionDep
    :return: User | None
    """
    if not await session.scalar(select(UserModel).where(UserModel.id == data.id)):
        return {'error': 'Пользователь не найден'}
    
    obj = await session.get(UserModel, data.id)

    await session.delete(obj)
    await session.commit()

    return obj


async def get_all_users(session: SesionDep) -> list[dict[str, bool | str]]:
    """
    Возвращает всех пользователей из базы данных

    :param session: SesionDep
    :return: list[dict[str, bool | str]]
    """
    # Создаем запрос для выборки всех пользователей
    query = select(UserModel)

    # Выполняем запрос и получаем результат
    result = await session.execute(query)

    # Извлекаем записи как объекты модели
    records = result.scalars().all()
    result = [{'username': i.username, 'password': i.password, 'email': i.email, 'admin': i.admin} for i in records]

    # Возвращаем список всех пользователей
    return result
