"""
Ambulance Tracking Model
"""
from beanie import Document
from pydantic import Field
from typing import Optional, Dict, Any
from datetime import datetime
from enum import Enum


class AmbulanceStatus(str, Enum):
    """Ambulance status"""
    AVAILABLE = "available"
    DISPATCHED = "dispatched"
    EN_ROUTE = "en_route"
    ON_SCENE = "on_scene"
    TRANSPORTING = "transporting"
    RETURNING = "returning"
    OFFLINE = "offline"


class AmbulanceTracking(Document):
    """Ambulance live tracking document"""
    
    ambulance_id: str = Field(..., description="Unique ambulance identifier")
    ambulance_number: str = Field(..., description="Ambulance registration number")
    driver_name: Optional[str] = Field(None, description="Driver name")
    driver_phone: Optional[str] = Field(None, description="Driver phone number")
    
    status: AmbulanceStatus = Field(default=AmbulanceStatus.AVAILABLE, description="Current status")
    
    current_location: Dict[str, Any] = Field(..., description="Current GPS location")
    current_lat: Optional[float] = Field(None, description="Current latitude")
    current_lng: Optional[float] = Field(None, description="Current longitude")
    
    assigned_case: Optional[str] = Field(None, description="Assigned emergency case ID")
    destination_hospital_id: Optional[str] = Field(None, description="Destination hospital ID")
    
    eta_minutes: Optional[int] = Field(None, description="Estimated time of arrival in minutes")
    route_distance_km: Optional[float] = Field(None, description="Route distance in kilometers")
    
    last_update: datetime = Field(default_factory=datetime.utcnow, description="Last GPS update")
    created_at: datetime = Field(default_factory=datetime.utcnow, description="Creation timestamp")
    
    metadata: Dict[str, Any] = Field(default_factory=dict, description="Additional metadata")
    
    class Settings:
        name = "Ambulance_Live_Tracking"
        indexes = [
            "ambulance_id",
            "status",
            "assigned_case",
            ["current_lat", "current_lng"],
            "last_update",
        ]

