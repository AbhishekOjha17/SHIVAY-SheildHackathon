"""
Emergency case schemas
"""
from pydantic import BaseModel, Field, EmailStr
from typing import Optional, Dict, Any, List
from datetime import datetime

from app.models.emergency import EmergencyStatus, SeverityLevel, EmergencyType


class EmergencyCaseCreate(BaseModel):
    """Schema for creating emergency case"""
    caller_id: Optional[str] = None
    caller_name: Optional[str] = None
    caller_phone: Optional[str] = None
    caller_email: Optional[EmailStr] = None
    emergency_type: EmergencyType
    severity_level: SeverityLevel
    location: Dict[str, Any]
    location_lat: Optional[float] = None
    location_lng: Optional[float] = None
    location_address: Optional[str] = None
    description: Optional[str] = None
    people_involved: Optional[int] = None
    injuries_reported: Optional[int] = None


class EmergencyCaseUpdate(BaseModel):
    """Schema for updating emergency case"""
    status: Optional[EmergencyStatus] = None
    severity_level: Optional[SeverityLevel] = None
    assigned_ambulance_id: Optional[str] = None
    assigned_hospital_id: Optional[str] = None
    assigned_officers: Optional[List[str]] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None


class EmergencyCaseResponse(BaseModel):
    """Schema for emergency case response"""
    case_id: str
    caller_id: Optional[str] = None
    caller_name: Optional[str] = None
    caller_phone: Optional[str] = None
    emergency_type: EmergencyType
    severity_level: SeverityLevel
    status: EmergencyStatus
    location: Dict[str, Any]
    location_lat: Optional[float] = None
    location_lng: Optional[float] = None
    location_address: Optional[str] = None
    description: Optional[str] = None
    people_involved: Optional[int] = None
    injuries_reported: Optional[int] = None
    assigned_ambulance_id: Optional[str] = None
    assigned_hospital_id: Optional[str] = None
    assigned_officers: List[str] = []
    ai_recommendations: List[str] = []
    ai_confidence: Optional[float] = None
    created_at: datetime
    updated_at: datetime
    resolved_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True


class EmergencyCaseListResponse(BaseModel):
    """Schema for emergency case list response"""
    cases: List[EmergencyCaseResponse]
    total: int
    skip: int
    limit: int

