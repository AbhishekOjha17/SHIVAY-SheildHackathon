"""
Event timestamping service
"""
from datetime import datetime
from typing import Dict, Any
from loguru import logger


class EventTimestampingService:
    """Adds timestamps to events"""
    
    @staticmethod
    def add_timestamps(data: Dict[str, Any]) -> Dict[str, Any]:
        """Add created_at and updated_at timestamps"""
        now = datetime.utcnow()
        
        if "created_at" not in data:
            data["created_at"] = now
        
        data["updated_at"] = now
        
        return data
    
    @staticmethod
    def add_event_timestamp(data: Dict[str, Any], event_type: str) -> Dict[str, Any]:
        """Add event-specific timestamp"""
        now = datetime.utcnow()
        
        timestamp_key = f"{event_type}_at"
        data[timestamp_key] = now
        
        return data
    
    @staticmethod
    def get_timestamp() -> datetime:
        """Get current UTC timestamp"""
        return datetime.utcnow()

