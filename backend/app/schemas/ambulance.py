"""
Ambulance schemas
"""
from pydantic import BaseModel
from typing import Optional, Dict, Any, List
from datetime import datetime


class AmbulanceResponse(BaseModel):
    """Schema for ambulance response"""
    ambulance_id: str
    ambulance_number: str
    driver_name: Optional[str] = None
    driver_phone: Optional[str] = None
    status: str
    current_location: Dict[str, Any]
    current_lat: Optional[float] = None
    current_lng: Optional[float] = None
    assigned_case: Optional[str] = None
    destination_hospital_id: Optional[str] = None
    eta_minutes: Optional[int] = None
    route_distance_km: Optional[float] = None
    last_update: datetime
    created_at: datetime
    
    class Config:
        from_attributes = True


class AmbulanceListResponse(BaseModel):
    """Schema for ambulance list response"""
    ambulances: List[AmbulanceResponse]
    total: int
    skip: int
    limit: int


class AmbulanceDispatchRequest(BaseModel):
    """Schema for ambulance dispatch request"""
    ambulance_id: str
    case_id: str
    destination_hospital_id: Optional[str] = None


class AmbulanceTrackingUpdate(BaseModel):
    """Schema for updating ambulance tracking"""
    current_lat: float
    current_lng: float
    status: Optional[str] = None
    eta_minutes: Optional[int] = None
    route_distance_km: Optional[float] = None

