"""
Call schemas
"""
from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class CallCreate(BaseModel):
    """Schema for creating call"""
    call_id: str
    from_number: str
    to_number: str
    direction: str  # "inbound" or "outbound"
    case_id: Optional[str] = None


class CallResponse(BaseModel):
    """Schema for call response"""
    call_id: str
    from_number: str
    to_number: str
    direction: str
    status: str
    case_id: Optional[str] = None
    recording_url: Optional[str] = None
    duration: Optional[float] = None
    created_at: datetime
    
    class Config:
        from_attributes = True


class CallStatusUpdate(BaseModel):
    """Schema for updating call status"""
    call_id: str
    status: str

