"""
Police schemas
"""
from pydantic import BaseModel
from typing import Optional, Dict, Any, List
from datetime import datetime


class PoliceOfficerResponse(BaseModel):
    """Schema for police officer response"""
    officer_id: str
    officer_name: str
    officer_rank: str
    officer_phone: Optional[str] = None
    officer_station: Optional[str] = None
    
    class Config:
        from_attributes = True


class PoliceOfficerListResponse(BaseModel):
    """Schema for police officer list response"""
    officers: List[PoliceOfficerResponse]
    total: int
    skip: int
    limit: int


class PoliceAlertRequest(BaseModel):
    """Schema for police alert request"""
    case_id: str
    severity: str
    num_officers: int = 3


class PoliceActionCreate(BaseModel):
    """Schema for creating police action"""
    officer_id: str
    case_id: str
    action_type: str
    action_description: Optional[str] = None
    location: Optional[Dict[str, Any]] = None

