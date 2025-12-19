"""
Request validation engine
"""
from typing import Dict, Any, Optional, List
from pydantic import ValidationError
from loguru import logger


class RequestValidationEngine:
    """Validates incoming requests"""
    
    @staticmethod
    def validate_emergency_request(data: Dict[str, Any]) -> tuple[bool, Optional[List[str]]]:
        """Validate emergency request data"""
        errors = []
        
        # Required fields
        if "emergency_type" not in data:
            errors.append("emergency_type is required")
        
        if "location" not in data:
            errors.append("location is required")
        elif not isinstance(data["location"], dict):
            errors.append("location must be an object")
        
        # Validate location coordinates
        if "location" in data and isinstance(data["location"], dict):
            location = data["location"]
            if "lat" in location and "lng" in location:
                try:
                    lat = float(location["lat"])
                    lng = float(location["lng"])
                    if not (-90 <= lat <= 90):
                        errors.append("latitude must be between -90 and 90")
                    if not (-180 <= lng <= 180):
                        errors.append("longitude must be between -180 and 180")
                except (ValueError, TypeError):
                    errors.append("invalid latitude/longitude format")
        
        # Validate phone number if provided
        if "caller_phone" in data and data["caller_phone"]:
            phone = data["caller_phone"]
            if not isinstance(phone, str) or len(phone) < 10:
                errors.append("invalid phone number format")
        
        return len(errors) == 0, errors if errors else None
    
    @staticmethod
    def validate_location(location: Dict[str, Any]) -> tuple[bool, Optional[str]]:
        """Validate location data"""
        if not isinstance(location, dict):
            return False, "location must be an object"
        
        if "lat" not in location or "lng" not in location:
            return False, "location must contain lat and lng"
        
        try:
            lat = float(location["lat"])
            lng = float(location["lng"])
            
            if not (-90 <= lat <= 90):
                return False, "latitude must be between -90 and 90"
            if not (-180 <= lng <= 180):
                return False, "longitude must be between -180 and 180"
            
            return True, None
        except (ValueError, TypeError):
            return False, "invalid latitude/longitude format"
    
    @staticmethod
    def validate_phone_number(phone: str) -> tuple[bool, Optional[str]]:
        """Validate phone number"""
        if not phone:
            return False, "phone number is required"
        
        # Remove non-digit characters for validation
        digits_only = ''.join(filter(str.isdigit, phone))
        
        if len(digits_only) < 10:
            return False, "phone number must have at least 10 digits"
        
        return True, None

