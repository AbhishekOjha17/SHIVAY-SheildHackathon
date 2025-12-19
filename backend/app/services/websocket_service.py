"""
WebSocket service for real-time updates
"""
from fastapi import WebSocket
from typing import Dict, List, Set
from loguru import logger


class WebSocketService:
    """Service for managing WebSocket connections"""
    
    def __init__(self):
        self.active_connections: List[WebSocket] = []
        self.subscriptions: Dict[WebSocket, Set[str]] = {}
    
    async def connect(self, websocket: WebSocket):
        """Accept new WebSocket connection"""
        await websocket.accept()
        self.active_connections.append(websocket)
        self.subscriptions[websocket] = set()
        logger.info(f"WebSocket connected. Total connections: {len(self.active_connections)}")
    
    def disconnect(self, websocket: WebSocket):
        """Remove WebSocket connection"""
        if websocket in self.active_connections:
            self.active_connections.remove(websocket)
        if websocket in self.subscriptions:
            del self.subscriptions[websocket]
        logger.info(f"WebSocket disconnected. Total connections: {len(self.active_connections)}")
    
    async def subscribe(self, websocket: WebSocket, channel: str):
        """Subscribe WebSocket to a channel"""
        if websocket in self.subscriptions:
            self.subscriptions[websocket].add(channel)
            logger.info(f"Subscribed to channel: {channel}")
    
    async def unsubscribe(self, websocket: WebSocket, channel: str):
        """Unsubscribe WebSocket from a channel"""
        if websocket in self.subscriptions:
            self.subscriptions[websocket].discard(channel)
            logger.info(f"Unsubscribed from channel: {channel}")
    
    async def broadcast(self, channel: str, message: dict):
        """Broadcast message to all subscribers of a channel"""
        disconnected = []
        for websocket, channels in self.subscriptions.items():
            if channel in channels:
                try:
                    await websocket.send_json(message)
                except Exception as e:
                    logger.error(f"Error broadcasting to WebSocket: {e}")
                    disconnected.append(websocket)
        
        # Remove disconnected WebSockets
        for ws in disconnected:
            self.disconnect(ws)

