"""
Police Officer Action Model
"""
from beanie import Document
from pydantic import Field
from typing import Optional, Dict, Any
from datetime import datetime
from enum import Enum


class OfficerRank(str, Enum):
    """Police officer rank"""
    CONSTABLE = "constable"
    HEAD_CONSTABLE = "head_constable"
    ASI = "asi"
    SI = "si"
    INSPECTOR = "inspector"
    DSP = "dsp"
    SP = "sp"
    SSP = "ssp"
    DIG = "dig"
    IGP = "igp"


class ActionType(str, Enum):
    """Action type"""
    ALERTED = "alerted"
    DISPATCHED = "dispatched"
    ON_SCENE = "on_scene"
    TRAFFIC_CLEARANCE = "traffic_clearance"
    INVESTIGATION = "investigation"
    CASE_CLOSED = "case_closed"
    OTHER = "other"


class PoliceOfficerAction(Document):
    """Police officer action document"""
    
    officer_id: str = Field(..., description="Unique officer identifier")
    officer_name: str = Field(..., description="Officer name")
    officer_rank: OfficerRank = Field(..., description="Officer rank")
    officer_phone: Optional[str] = Field(None, description="Officer phone number")
    officer_station: Optional[str] = Field(None, description="Police station")
    
    case_id: str = Field(..., description="Associated emergency case ID")
    action_type: ActionType = Field(..., description="Type of action taken")
    
    action_description: Optional[str] = Field(None, description="Action description")
    location: Optional[Dict[str, Any]] = Field(None, description="Action location")
    
    timestamp: datetime = Field(default_factory=datetime.utcnow, description="Action timestamp")
    created_at: datetime = Field(default_factory=datetime.utcnow, description="Creation timestamp")
    
    metadata: Dict[str, Any] = Field(default_factory=dict, description="Additional metadata")
    
    class Settings:
        name = "Police_Officer_Actions"
        indexes = [
            "officer_id",
            "case_id",
            "action_type",
            "timestamp",
        ]

