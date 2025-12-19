"""
Data cleaning and normalization
"""
from typing import Dict, Any, Optional
from loguru import logger
import re


class DataCleaningProcessor:
    """Processes and cleans raw input data"""
    
    @staticmethod
    def clean_phone_number(phone: str) -> Optional[str]:
        """Clean and normalize phone number"""
        if not phone:
            return None
        
        # Remove all non-digit characters
        cleaned = re.sub(r'\D', '', phone)
        
        # Add country code if missing (assuming India +91)
        if len(cleaned) == 10:
            cleaned = f"91{cleaned}"
        
        return cleaned if cleaned else None
    
    @staticmethod
    def clean_location_data(location: Dict[str, Any]) -> Dict[str, Any]:
        """Clean and normalize location data"""
        cleaned = location.copy()
        
        # Ensure lat/lng are floats
        if "lat" in cleaned:
            try:
                cleaned["lat"] = float(cleaned["lat"])
            except (ValueError, TypeError):
                cleaned["lat"] = None
        
        if "lng" in cleaned:
            try:
                cleaned["lng"] = float(cleaned["lng"])
            except (ValueError, TypeError):
                cleaned["lng"] = None
        
        # Normalize address
        if "address" in cleaned and cleaned["address"]:
            cleaned["address"] = cleaned["address"].strip()
        
        return cleaned
    
    @staticmethod
    def clean_text(text: str) -> str:
        """Clean text input"""
        if not text:
            return ""
        
        # Remove extra whitespace
        text = re.sub(r'\s+', ' ', text)
        
        # Remove special characters (keep basic punctuation)
        text = re.sub(r'[^\w\s.,!?]', '', text)
        
        return text.strip()
    
    @staticmethod
    def normalize_emergency_type(emergency_type: str) -> str:
        """Normalize emergency type"""
        type_mapping = {
            "accident": "accident",
            "medical": "medical",
            "fire": "fire",
            "crime": "crime",
            "natural_disaster": "natural_disaster",
            "disaster": "natural_disaster",
            "other": "other",
        }
        
        normalized = emergency_type.lower().strip()
        return type_mapping.get(normalized, "other")

