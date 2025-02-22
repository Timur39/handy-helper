from fastapi import FastAPI
from app.routers.auth.user_routers import router as user_router
from fastapi.middleware.cors import CORSMiddleware
from app.routers.api.api_routers import router as api_router
from app.routers.routers import router as other_router

app = FastAPI(title="My Project API", version="0.1.0")


app.include_router(user_router)
app.include_router(api_router)
app.include_router(other_router)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost", "http://localhost:3000", "http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
