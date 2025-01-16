from fastapi import FastAPI
from app.routers.user_routers import router as user_router
from fastapi.middleware.cors import CORSMiddleware
from app.routers.modrinth_routers import router as modrinth_router
from app.routers.github_routers import router as github_router
from app.routers.gmail_routers import router as gmail_router
from app.routers.news_routers import router as news_router
app = FastAPI(title="My Project API", version="1.0.0")

app.include_router(user_router)
app.include_router(modrinth_router)
app.include_router(github_router)
app.include_router(gmail_router)
app.include_router(news_router)



app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost", "http://localhost:3000", "http://localhost:5173"],  # Укажите домены, которые могут делать запросы
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
