"""
WebSocket API for real-time updates
"""
from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from typing import List
import json

from app.services.websocket_service import WebSocketService

router = APIRouter()
websocket_service = WebSocketService()


@router.websocket("/")
async def websocket_endpoint(websocket: WebSocket):
    """WebSocket endpoint for real-time updates"""
    await websocket_service.connect(websocket)
    
    try:
        while True:
            # Receive message from client
            data = await websocket.receive_text()
            message = json.loads(data)
            
            # Handle different message types
            if message.get("type") == "subscribe":
                await websocket_service.subscribe(websocket, message.get("channel"))
            elif message.get("type") == "unsubscribe":
                await websocket_service.unsubscribe(websocket, message.get("channel"))
            else:
                # Echo back or process message
                await websocket.send_text(json.dumps({"echo": message}))
                
    except WebSocketDisconnect:
        websocket_service.disconnect(websocket)

