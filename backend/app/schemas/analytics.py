"""
Analytics schemas
"""
from pydantic import BaseModel
from typing import Optional, Dict, Any, List
from datetime import datetime


class DashboardDataResponse(BaseModel):
    """Schema for dashboard data response"""
    total_cases: int
    active_cases: int
    resolved_cases: int
    cases_by_severity: Dict[str, int]
    cases_by_type: Dict[str, int]
    response_times: Dict[str, float]
    ambulance_status: Dict[str, int]
    hospital_load: List[Dict[str, Any]]
    recent_cases: List[Dict[str, Any]]


class ReportRequest(BaseModel):
    """Schema for report request"""
    report_type: str
    start_date: datetime
    end_date: datetime
    format: str = "pdf"  # "pdf" or "csv"


class TrendAnalysisRequest(BaseModel):
    """Schema for trend analysis request"""
    metric: str
    start_date: datetime
    end_date: datetime


class TrendAnalysisResponse(BaseModel):
    """Schema for trend analysis response"""
    metric: str
    data_points: List[Dict[str, Any]]
    trend: str  # "increasing", "decreasing", "stable"
    change_percentage: float

