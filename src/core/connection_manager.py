from fastapi import WebSocket
from typing import List
import json
import logging

logger = logging.getLogger(__name__)

class ConnectionManager:
    """
    Manages active WebSocket connections for broadcasting alerts.
    """
    def __init__(self):
        # List to store active websocket connections
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        """ Accepts a new connection. """
        await websocket.accept()
        self.active_connections.append(websocket)
        logger.info(f"New WebSocket connection. Total active: {len(self.active_connections)}")

    def disconnect(self, websocket: WebSocket):
        """ Removes a disconnected connection. """
        if websocket in self.active_connections:
            self.active_connections.remove(websocket)
            logger.info(f"WebSocket disconnected. Remaining: {len(self.active_connections)}")

    async def broadcast(self, message: dict):
        """ Sends a JSON message to all active connections. """
        if not self.active_connections:
            return
            
        message_str = json.dumps(message)
        
        # We use list() to avoid issues if a client disconnects during the broadcast
        for connection in list(self.active_connections):
            try:
                await connection.send_text(message_str)
            except Exception as e:
                logger.error(f"Error broadcasting to client: {e}")
                self.disconnect(connection)

# Global instances
connection_manager = ConnectionManager()
