"""
Shared constants for emergency response
"""

# Emergency Types
EMERGENCY_TYPES = [
    "accident",
    "medical",
    "fire",
    "crime",
    "natural_disaster",
    "other",
]

# Severity Levels
SEVERITY_LEVELS = [
    "critical",
    "high",
    "medium",
    "low",
]

# Status Values
CASE_STATUSES = [
    "open",
    "dispatched",
    "in_progress",
    "resolved",
    "cancelled",
]

# API Endpoints
API_ENDPOINTS = {
    "EMERGENCY": "/api/v1/emergency/",
    "CALLS": "/api/v1/calls/",
    "AMBULANCE": "/api/v1/ambulance/",
    "HOSPITAL": "/api/v1/hospital/",
    "POLICE": "/api/v1/police/",
    "AI": "/api/v1/ai/",
    "ANALYTICS": "/api/v1/analytics/",
}

