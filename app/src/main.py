from fastapi import FastAPI, WebSocket, WebSocketDisconnect, Request
from src.routers.user_routers import router as user_router
from fastapi.middleware.cors import CORSMiddleware
from src.routers.service_routers import router as api_router
from src.routers.routers import router as other_router
from src.utils.websocket import manager
from contextlib import asynccontextmanager
import time


@asynccontextmanager
async def lifespan(app: FastAPI):
    print('Server is starting...')

    app.include_router(user_router)                                                                                     
    app.include_router(api_router)
    app.include_router(other_router)

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

# Редирект на https и wss
# app.add_middleware(HTTPSRedirectMiddleware)

@app.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: int):
    await manager.connect(websocket)
    try:
        await manager.broadcast(f"Клиент #{client_id} присоединился к чату")
        while True:
            data = await websocket.receive_text()
            await manager.broadcast(f"#{client_id}: {data}")
    except WebSocketDisconnect:
        await manager.disconnect(websocket)
        await manager.broadcast(f"Клиент #{client_id} покинул чат")

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.perf_counter()
    response = await call_next(request)
    process_time = time.perf_counter() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response
