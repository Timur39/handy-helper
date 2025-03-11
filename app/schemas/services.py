from pydantic import BaseModel
from datetime import datetime

class Github_Schema(BaseModel):
    actor: str
    type: str
    description: str
    repo: str
    actor_url: str
    created_at: datetime

class Gmail_Schema(BaseModel):
    title: str
    date: datetime
    link : str


class Todoist_Schema(BaseModel):
    title: str
    link: str
    priority: int
    description: str 

class Modrinth_Schema(BaseModel):
    title: str
    game_versions: list[str]
    updated: datetime
    loaders: list[str]
    description: str
    link: str


class News_Schema(BaseModel):
    text: str
    link: str
    date: datetime
    channel: str


class Price_Schema(BaseModel):
    title: str
    ticker: str
    price: str


class Youtube_Schema(BaseModel):
    title: str
    date: str
    views: str
    duration: str
    url: str
    preview_url: str
    channel: str

class Stepik_Schema(BaseModel):
    id: int
    knowledge: int
    solved_steps_count: int
    issued_certificates_count: int
    link: str


