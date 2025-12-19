"""
Emergency Case API endpoints
"""
from fastapi import APIRouter, Depends, HTTPException, status, Query
from typing import List, Optional
from datetime import datetime

from app.models.emergency import EmergencyCase, EmergencyStatus, SeverityLevel, EmergencyType
from app.schemas.emergency import (
    EmergencyCaseCreate,
    EmergencyCaseUpdate,
    EmergencyCaseResponse,
    EmergencyCaseListResponse,
)
from app.services.emergency_service import EmergencyService
from app.core.dependencies import get_current_active_user

router = APIRouter()


@router.post("/", response_model=EmergencyCaseResponse, status_code=status.HTTP_201_CREATED)
async def create_emergency_case(
    case_data: EmergencyCaseCreate,
    current_user: dict = Depends(get_current_active_user),
):
    """Create a new emergency case"""
    service = EmergencyService()
    case = await service.create_case(case_data)
    return case


@router.get("/", response_model=EmergencyCaseListResponse)
async def list_emergency_cases(
    status: Optional[EmergencyStatus] = Query(None, description="Filter by status"),
    severity: Optional[SeverityLevel] = Query(None, description="Filter by severity"),
    emergency_type: Optional[EmergencyType] = Query(None, description="Filter by type"),
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=1000),
    current_user: dict = Depends(get_current_active_user),
):
    """List all emergency cases with optional filters"""
    service = EmergencyService()
    cases = await service.list_cases(
        status=status,
        severity=severity,
        emergency_type=emergency_type,
        skip=skip,
        limit=limit,
    )
    return cases


@router.get("/{case_id}", response_model=EmergencyCaseResponse)
async def get_emergency_case(
    case_id: str,
    current_user: dict = Depends(get_current_active_user),
):
    """Get emergency case by ID"""
    service = EmergencyService()
    case = await service.get_case_by_id(case_id)
    if not case:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Emergency case {case_id} not found",
        )
    return case


@router.put("/{case_id}", response_model=EmergencyCaseResponse)
async def update_emergency_case(
    case_id: str,
    case_data: EmergencyCaseUpdate,
    current_user: dict = Depends(get_current_active_user),
):
    """Update emergency case"""
    service = EmergencyService()
    case = await service.update_case(case_id, case_data)
    if not case:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Emergency case {case_id} not found",
        )
    return case


@router.delete("/{case_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_emergency_case(
    case_id: str,
    current_user: dict = Depends(get_current_active_user),
):
    """Delete emergency case"""
    service = EmergencyService()
    success = await service.delete_case(case_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Emergency case {case_id} not found",
        )


@router.post("/{case_id}/resolve", response_model=EmergencyCaseResponse)
async def resolve_emergency_case(
    case_id: str,
    current_user: dict = Depends(get_current_active_user),
):
    """Mark emergency case as resolved"""
    service = EmergencyService()
    case = await service.resolve_case(case_id)
    if not case:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Emergency case {case_id} not found",
        )
    return case

