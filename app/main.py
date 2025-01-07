from fastapi import FastAPI
from app.routers.user_routers import router as user_router
from app.db.session import engine
from app.db.models import Base
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(title="My Project API", version="1.0.0")


app.include_router(user_router, prefix="/api")




app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost", "http://localhost:3000"],  # Укажите домены, которые могут делать запросы
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)
