from src.database import SesionDep
from sqlalchemy import select

from src.models.users import UserModel
from src.schemas.user import UserCreate, UserOut
from src.config import list_of_admins


async def create_user(data: UserCreate, session: SesionDep) -> dict[str, str]:
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


async def get_all_users(session: SesionDep) -> list[UserModel]:
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
