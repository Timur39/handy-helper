from fastapi import WebSocket, WebSocketDisconnect, APIRouter
from app.src.utils.websocket import manager

router = APIRouter(prefix='/ws', tags=['websocket'])

@router.websocket("/{client_id}")
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