"""
AI Recommendation Model
"""
from beanie import Document
from pydantic import Field
from typing import Optional, Dict, Any, List
from datetime import datetime
from enum import Enum


class RecommendationType(str, Enum):
    """Recommendation type"""
    DISPATCH_AMBULANCE = "dispatch_ambulance"
    ALERT_HOSPITAL = "alert_hospital"
    NOTIFY_POLICE = "notify_police"
    REQUEST_ROAD_CLEARANCE = "request_road_clearance"
    ASK_FOR_MORE_DATA = "ask_for_more_data"
    ESCALATE = "escalate"
    OTHER = "other"


class RecommendationStatus(str, Enum):
    """Recommendation status"""
    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"
    EXECUTED = "executed"
    EXPIRED = "expired"


class AIRecommendation(Document):
    """AI recommendation document"""
    
    case_id: str = Field(..., description="Associated emergency case ID")
    recommendation_id: str = Field(..., description="Unique recommendation identifier")
    
    recommendation_type: RecommendationType = Field(..., description="Type of recommendation")
    status: RecommendationStatus = Field(
        default=RecommendationStatus.PENDING,
        description="Recommendation status"
    )
    
    severity_score: float = Field(..., description="Severity score (0-1)")
    confidence: float = Field(..., description="Confidence score (0-1)")
    
    recommended_action: str = Field(..., description="Recommended action description")
    reasoning: Optional[str] = Field(None, description="AI reasoning for recommendation")
    
    target_entity: Optional[str] = Field(None, description="Target entity (ambulance_id, hospital_id, etc.)")
    target_entity_type: Optional[str] = Field(None, description="Type of target entity")
    
    priority: int = Field(default=0, description="Priority level (higher = more urgent)")
    
    related_incidents: List[str] = Field(default_factory=list, description="Related incident case IDs")
    
    created_at: datetime = Field(default_factory=datetime.utcnow, description="Creation timestamp")
    executed_at: Optional[datetime] = Field(None, description="Execution timestamp")
    expires_at: Optional[datetime] = Field(None, description="Expiration timestamp")
    
    metadata: Dict[str, Any] = Field(default_factory=dict, description="Additional metadata")
    
    class Settings:
        name = "AI_Recommendations"
        indexes = [
            "case_id",
            "recommendation_id",
            "recommendation_type",
            "status",
            "severity_score",
            "created_at",
        ]

