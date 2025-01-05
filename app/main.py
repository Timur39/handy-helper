from fastapi import FastAPI
from app.api.routers import router as users_router


app = FastAPI()

app.include_router(users_router, prefix="/api")

# @app.get("/")
# async def root():
#     return {"message": "Hello, World!"}