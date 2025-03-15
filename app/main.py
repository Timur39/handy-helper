import time
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from app.src.routers.user_routers import router as user_router
from app.src.routers.service_routers import router as api_router
from app.src.routers.routers import router as other_router
from app.src.routers.chat_routers import router as ws_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    print('Server is starting...')

    app.include_router(user_router)                                                                                     
    app.include_router(api_router)
    app.include_router(other_router)
    app.include_router(ws_router)


    yield

    print('Server is shutting down...')


app = FastAPI(lifespan=lifespan, title="My Project API", version="0.3.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost", "http://localhost:3000", "http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.perf_counter()
    response = await call_next(request)
    process_time = time.perf_counter() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response




# Редирект на https и wss
# app.add_middleware(HTTPSRedirectMiddleware)
