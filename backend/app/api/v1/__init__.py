"""
API v1 router
"""
from fastapi import APIRouter

from app.api.v1 import (
    emergency,
    calls,
    ambulance,
    hospital,
    police,
    ai,
    analytics,
    websocket,
)

api_router = APIRouter()

# Include all route modules
api_router.include_router(emergency.router, prefix="/emergency", tags=["Emergency"])
api_router.include_router(calls.router, prefix="/calls", tags=["Calls"])
api_router.include_router(ambulance.router, prefix="/ambulance", tags=["Ambulance"])
api_router.include_router(hospital.router, prefix="/hospital", tags=["Hospital"])
api_router.include_router(police.router, prefix="/police", tags=["Police"])
api_router.include_router(ai.router, prefix="/ai", tags=["AI"])
api_router.include_router(analytics.router, prefix="/analytics", tags=["Analytics"])
api_router.include_router(websocket.router, prefix="/websocket", tags=["WebSocket"])

