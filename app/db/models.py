from sqlalchemy import Integer, String, Boolean
from sqlalchemy.orm import Mapped, mapped_column
from app.db.session import Base


class User(Base):
    __tablename__ = "users"
    username: Mapped[str] = mapped_column(String, index=True)
    email: Mapped[str] = mapped_column(String, unique=True, index=True)
    password: Mapped[str]
    admin: Mapped[bool] = mapped_column(Boolean, default=False)
