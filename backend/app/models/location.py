"""
Location Metadata Model
"""
from beanie import Document
from pydantic import Field
from typing import Optional, Dict, Any
from datetime import datetime


class LocationMetadata(Document):
    """Location metadata document"""
    
    location_id: str = Field(..., description="Unique location identifier")
    case_id: Optional[str] = Field(None, description="Associated emergency case ID")
    
    latitude: float = Field(..., description="Latitude")
    longitude: float = Field(..., description="Longitude")
    
    formatted_address: Optional[str] = Field(None, description="Formatted address")
    address_components: Dict[str, Any] = Field(default_factory=dict, description="Address components")
    
    city: Optional[str] = Field(None, description="City")
    state: Optional[str] = Field(None, description="State")
    country: Optional[str] = Field(None, description="Country")
    postal_code: Optional[str] = Field(None, description="Postal code")
    
    place_id: Optional[str] = Field(None, description="Google Maps place ID")
    
    accuracy: Optional[float] = Field(None, description="Location accuracy in meters")
    altitude: Optional[float] = Field(None, description="Altitude in meters")
    
    geocoded_at: datetime = Field(default_factory=datetime.utcnow, description="Geocoding timestamp")
    created_at: datetime = Field(default_factory=datetime.utcnow, description="Creation timestamp")
    
    metadata: Dict[str, Any] = Field(default_factory=dict, description="Additional metadata")
    
    class Settings:
        name = "Location_Metadata"
        indexes = [
            "location_id",
            "case_id",
            ["latitude", "longitude"],
            "city",
            "state",
        ]

