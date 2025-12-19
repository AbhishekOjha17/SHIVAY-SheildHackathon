"""
Shared validation schemas for emergency cases
"""
from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class LocationSchema(BaseModel):
    """Location schema"""
    lat: float = Field(..., ge=-90, le=90)
    lng: float = Field(..., ge=-180, le=180)
    address: Optional[str] = None


class EmergencyCaseSchema(BaseModel):
    """Emergency case schema"""
    case_id: str
    caller_id: Optional[str] = None
    emergency_type: str
    severity_level: str
    status: str
    location: Dict[str, Any]
    description: Optional[str] = None
    created_at: str
    updated_at: str

