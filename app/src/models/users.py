from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column
from app.src.database import Base


class UserModel(Base):
    __tablename__ = "users"

    username: Mapped[str] = mapped_column(String, index=True)
    email: Mapped[str] = mapped_column(String, unique=True, index=True)
    password: Mapped[str]
    admin: Mapped[bool] = mapped_column(Boolean, default=False)

