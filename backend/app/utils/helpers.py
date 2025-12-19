"""
Helper utility functions
"""
import uuid
from typing import Optional
from datetime import datetime


def generate_case_id() -> str:
    """Generate unique case ID"""
    return f"CASE-{uuid.uuid4().hex[:8].upper()}"


def generate_call_id() -> str:
    """Generate unique call ID"""
    return f"CALL-{uuid.uuid4().hex[:8].upper()}"


def generate_recommendation_id() -> str:
    """Generate unique recommendation ID"""
    return f"REC-{uuid.uuid4().hex[:8].upper()}"


def format_datetime(dt: datetime) -> str:
    """Format datetime to ISO string"""
    return dt.isoformat() if dt else None


def parse_datetime(dt_str: str) -> Optional[datetime]:
    """Parse ISO datetime string"""
    try:
        return datetime.fromisoformat(dt_str.replace('Z', '+00:00'))
    except (ValueError, AttributeError):
        return None

