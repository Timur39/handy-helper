from sqlalchemy import select
from app.src.config import list_of_admins
from app.src.database import SesionDep
from app.src.models.users import UserModel
from app.src.schemas.user import User


async def create_user(data: User, session: SesionDep) -> dict[str, str]:
    """
    Создает нового пользователя

    :param session: SesionDep
    :param data: UserCreate
    :return: dict[str, str]
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


async def delete_user_by_id(user_id: int, session: SesionDep) -> UserModel | dict[str, str]:
    """
    Удаляет пользователя из базы данных по его идентификатору

    :param id: int
    :param session: SesionDep
    :return: User | dict[str, str]
    """
    if not await session.scalar(select(UserModel).where(UserModel.id == user_id)):
        return {'error': 'Пользователь не найден'}
    
    obj = await session.get(UserModel, user_id)

    await session.delete(obj)
    await session.commit()

    return obj


async def get_all_users(session: SesionDep) -> list[User]:
    """
    Возвращает всех пользователей из базы данных

    :param session: SesionDep
    :return: list[UserModel]
    """
    # Создаем запрос для выборки всех пользователей
    query = select(UserModel)

    # Выполняем запрос и получаем результат
    result = await session.execute(query)

    # Извлекаем записи как объекты модели
    records = result.scalars().all()    
    result = [UserModel(username=i.username, email=i.email, password=i.password, admin=i.admin) for i in records]

    # Возвращаем список всех пользователей
    return result


async def get_user_by_name(username: int, session: SesionDep) -> list[User]:
    """
    Возвращает пользователя из базы данных по его username

    :param session: SesionDep
    :return: list[UserModel]
    """
    if not await session.scalar(select(UserModel).where(UserModel.username == username)):
        return {'error': 'Пользователь не найден'}
    
    obj = await session.scalar(select(UserModel).where(UserModel.username == username))

    return obj