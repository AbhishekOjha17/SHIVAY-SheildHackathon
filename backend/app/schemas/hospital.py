"""
Hospital schemas
"""
from pydantic import BaseModel
from typing import Optional, Dict, Any, List
from datetime import datetime


class HospitalResponse(BaseModel):
    """Schema for hospital response"""
    hospital_id: str
    hospital_name: str
    hospital_address: str
    location_lat: Optional[float] = None
    location_lng: Optional[float] = None
    available_beds: int
    total_beds: int
    occupied_beds: int
    icu_available: int
    icu_total: int
    icu_status: str
    doctor_on_call: Optional[str] = None
    doctor_phone: Optional[str] = None
    emergency_contact: Optional[str] = None
    emergency_phone: Optional[str] = None
    specialties: List[str] = []
    equipment_available: List[str] = []
    is_active: bool
    last_updated: datetime
    created_at: datetime
    
    class Config:
        from_attributes = True


class HospitalListResponse(BaseModel):
    """Schema for hospital list response"""
    hospitals: List[HospitalResponse]
    total: int
    skip: int
    limit: int


class HospitalResourceUpdate(BaseModel):
    """Schema for updating hospital resources"""
    available_beds: Optional[int] = None
    occupied_beds: Optional[int] = None
    icu_available: Optional[int] = None
    icu_status: Optional[str] = None
    doctor_on_call: Optional[str] = None
    doctor_phone: Optional[str] = None

