from fastapi import APIRouter, WebSocket, WebSocketDisconnect, Query, HTTPException, status
from src.core.connection_manager import connection_manager
from src.core.config import settings
import logging

logger = logging.getLogger(__name__)
router = APIRouter(tags=["WebSocket Alerts"])

@router.websocket("/ws/alerts")
async def websocket_alerts(
    websocket: WebSocket, 
    api_key: str = Query(...)
):
    """
    WebSocket endpoint for real-time machine health alerts.
    Expects API key as query parameter for authentication.
    """
    # Simple check for the API key (handshake phase)
    if api_key != settings.PROJECT_API_KEY:
        logger.warning(f"Unauthorized WebSocket connection attempt with key: {api_key}")
        await websocket.close(code=status.WS_1008_POLICY_VIOLATION)
        return

    # Connection successful
    await connection_manager.connect(websocket)
    try:
        # Keep connection open and wait for incoming messages (client-side hearts)
        while True:
            # We don't expect client messages for now, just waiting for broadcast
            data = await websocket.receive_text()
            # If clients send something, we ignore or echo (pong)
            
    except WebSocketDisconnect:
        connection_manager.disconnect(websocket)
    except Exception as e:
        logger.error(f"WebSocket error: {e}")
        connection_manager.disconnect(websocket)
