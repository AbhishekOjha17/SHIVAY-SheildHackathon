"""
Emergency Case Model
"""
from beanie import Document
from pydantic import Field, EmailStr
from typing import Optional, List, Dict, Any
from datetime import datetime
from enum import Enum


class EmergencyStatus(str, Enum):
    """Emergency case status"""
    OPEN = "open"
    DISPATCHED = "dispatched"
    IN_PROGRESS = "in_progress"
    RESOLVED = "resolved"
    CANCELLED = "cancelled"


class EmergencyType(str, Enum):
    """Emergency type"""
    ACCIDENT = "accident"
    MEDICAL = "medical"
    FIRE = "fire"
    CRIME = "crime"
    NATURAL_DISASTER = "natural_disaster"
    OTHER = "other"


class SeverityLevel(str, Enum):
    """Severity level"""
    CRITICAL = "critical"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"


class EmergencyCase(Document):
    """Emergency case document"""
    
    case_id: str = Field(..., description="Unique case identifier")
    caller_id: Optional[str] = Field(None, description="Caller identifier")
    caller_name: Optional[str] = Field(None, description="Caller name")
    caller_phone: Optional[str] = Field(None, description="Caller phone number")
    caller_email: Optional[EmailStr] = Field(None, description="Caller email")
    
    emergency_type: EmergencyType = Field(..., description="Type of emergency")
    severity_level: SeverityLevel = Field(..., description="Severity level")
    status: EmergencyStatus = Field(default=EmergencyStatus.OPEN, description="Case status")
    
    location: Dict[str, Any] = Field(..., description="Location data")
    location_lat: Optional[float] = Field(None, description="Latitude")
    location_lng: Optional[float] = Field(None, description="Longitude")
    location_address: Optional[str] = Field(None, description="Formatted address")
    
    description: Optional[str] = Field(None, description="Emergency description")
    people_involved: Optional[int] = Field(None, description="Number of people involved")
    injuries_reported: Optional[int] = Field(None, description="Number of injuries")
    
    assigned_ambulance_id: Optional[str] = Field(None, description="Assigned ambulance")
    assigned_hospital_id: Optional[str] = Field(None, description="Assigned hospital")
    assigned_officers: List[str] = Field(default_factory=list, description="Assigned police officers")
    
    ai_recommendations: List[str] = Field(default_factory=list, description="AI recommendation IDs")
    ai_confidence: Optional[float] = Field(None, description="AI confidence score")
    
    created_at: datetime = Field(default_factory=datetime.utcnow, description="Creation timestamp")
    updated_at: datetime = Field(default_factory=datetime.utcnow, description="Last update timestamp")
    resolved_at: Optional[datetime] = Field(None, description="Resolution timestamp")
    
    metadata: Dict[str, Any] = Field(default_factory=dict, description="Additional metadata")
    
    class Settings:
        name = "Emergency_Cases"
        indexes = [
            "case_id",
            "caller_id",
            "status",
            "severity_level",
            "created_at",
            ["location_lat", "location_lng"],
        ]

