"""
Hospital Resource Model
"""
from beanie import Document
from pydantic import Field
from typing import Optional, Dict, Any
from datetime import datetime
from enum import Enum


class ICUStatus(str, Enum):
    """ICU availability status"""
    AVAILABLE = "available"
    LIMITED = "limited"
    FULL = "full"
    UNAVAILABLE = "unavailable"


class HospitalResource(Document):
    """Hospital resource document"""
    
    hospital_id: str = Field(..., description="Unique hospital identifier")
    hospital_name: str = Field(..., description="Hospital name")
    hospital_address: str = Field(..., description="Hospital address")
    
    location_lat: Optional[float] = Field(None, description="Latitude")
    location_lng: Optional[float] = Field(None, description="Longitude")
    
    available_beds: int = Field(default=0, description="Available beds")
    total_beds: int = Field(default=0, description="Total beds")
    occupied_beds: int = Field(default=0, description="Occupied beds")
    
    icu_available: int = Field(default=0, description="Available ICU beds")
    icu_total: int = Field(default=0, description="Total ICU beds")
    icu_status: ICUStatus = Field(default=ICUStatus.AVAILABLE, description="ICU status")
    
    doctor_on_call: Optional[str] = Field(None, description="On-call doctor name")
    doctor_phone: Optional[str] = Field(None, description="On-call doctor phone")
    
    emergency_contact: Optional[str] = Field(None, description="Emergency contact")
    emergency_phone: Optional[str] = Field(None, description="Emergency phone number")
    
    specialties: list[str] = Field(default_factory=list, description="Medical specialties")
    equipment_available: list[str] = Field(default_factory=list, description="Available equipment")
    
    is_active: bool = Field(default=True, description="Hospital active status")
    
    last_updated: datetime = Field(default_factory=datetime.utcnow, description="Last update timestamp")
    created_at: datetime = Field(default_factory=datetime.utcnow, description="Creation timestamp")
    
    metadata: Dict[str, Any] = Field(default_factory=dict, description="Additional metadata")
    
    class Settings:
        name = "Hospital_Resources"
        indexes = [
            "hospital_id",
            "is_active",
            "icu_status",
            ["location_lat", "location_lng"],
        ]

