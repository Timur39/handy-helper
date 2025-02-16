from fastapi import Depends

from sqlalchemy import Integer
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine, AsyncSession

from typing import Annotated

from config import settings

# URL для подключения к PostgreSQL
DATABASE_URL = settings.get_db_url()

# Асинхронный движок SQLAlchemy
engine = create_async_engine(DATABASE_URL)

# Фабрика для создания асинхронных сессий
new_session = async_sessionmaker(engine, expire_on_commit=False)


# Базовый класс для моделей
class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)


async def get_session():
    async with new_session() as session:
        yield session


async def setup_database() -> dict[str, str]:
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    return {'status': 'Database was successfully created'}

SesionDep = Annotated[AsyncSession, Depends(get_session)]

