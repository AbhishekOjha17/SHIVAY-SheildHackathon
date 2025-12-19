"""
Geocoding utilities
"""
from typing import Dict, Any, Optional
from loguru import logger

from app.core.config import settings


class GeocodingService:
    """Service for geocoding operations"""
    
    @staticmethod
    async def reverse_geocode(lat: float, lng: float) -> Optional[Dict[str, Any]]:
        """Reverse geocode coordinates to address"""
        # In a real implementation, this would use Google Maps or Mapbox API
        logger.info(f"Reverse geocoding: {lat}, {lng}")
        
        # Mock response
        return {
            "formatted_address": "Mock Address",
            "city": "Mock City",
            "state": "Mock State",
            "country": "India",
            "postal_code": "123456",
        }
    
    @staticmethod
    async def geocode(address: str) -> Optional[Dict[str, Any]]:
        """Geocode address to coordinates"""
        # In a real implementation, this would use Google Maps or Mapbox API
        logger.info(f"Geocoding address: {address}")
        
        # Mock response
        return {
            "lat": 28.6139,
            "lng": 77.2090,
            "formatted_address": address,
        }
    
    @staticmethod
    def calculate_distance(
        lat1: float,
        lng1: float,
        lat2: float,
        lng2: float,
    ) -> float:
        """Calculate distance between two points in kilometers (Haversine formula)"""
        from math import radians, cos, sin, asin, sqrt
        
        # Convert to radians
        lat1, lng1, lat2, lng2 = map(radians, [lat1, lng1, lat2, lng2])
        
        # Haversine formula
        dlat = lat2 - lat1
        dlng = lng2 - lng1
        a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlng/2)**2
        c = 2 * asin(sqrt(a))
        
        # Radius of earth in kilometers
        r = 6371
        
        return c * r

