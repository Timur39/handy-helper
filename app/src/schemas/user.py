from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    email: str


class UserCreate(UserBase):
    password: str


class UserOut(BaseModel):
    id: int

    class Config:
        from_attributes = True
