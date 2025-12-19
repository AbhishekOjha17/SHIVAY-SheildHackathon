"""
Analytics API endpoints
"""
from fastapi import APIRouter, Depends, HTTPException, status, Query
from typing import Optional
from datetime import datetime

from app.schemas.analytics import (
    DashboardDataResponse,
    ReportRequest,
    TrendAnalysisRequest,
    TrendAnalysisResponse,
)
from app.services.analytics_service import AnalyticsService
from app.core.dependencies import get_current_active_user

router = APIRouter()


@router.get("/dashboard", response_model=DashboardDataResponse)
async def get_dashboard_data(
    start_date: Optional[datetime] = Query(None, description="Start date"),
    end_date: Optional[datetime] = Query(None, description="End date"),
    current_user: dict = Depends(get_current_active_user),
):
    """Get dashboard analytics data"""
    service = AnalyticsService()
    data = await service.get_dashboard_data(start_date=start_date, end_date=end_date)
    return data


@router.get("/reports", response_model=dict)
async def generate_report(
    report_request: ReportRequest,
    current_user: dict = Depends(get_current_active_user),
):
    """Generate analytics report"""
    service = AnalyticsService()
    report = await service.generate_report(
        report_type=report_request.report_type,
        start_date=report_request.start_date,
        end_date=report_request.end_date,
        format=report_request.format,
    )
    return report


@router.post("/trends", response_model=TrendAnalysisResponse)
async def analyze_trends(
    trend_request: TrendAnalysisRequest,
    current_user: dict = Depends(get_current_active_user),
):
    """Analyze trends"""
    service = AnalyticsService()
    trends = await service.analyze_trends(
        metric=trend_request.metric,
        start_date=trend_request.start_date,
        end_date=trend_request.end_date,
    )
    return trends

