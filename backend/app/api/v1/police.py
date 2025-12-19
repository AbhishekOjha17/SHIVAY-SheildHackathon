"""
Police API endpoints
"""
from fastapi import APIRouter, Depends, HTTPException, status, Query
from typing import List, Optional

from app.schemas.police import (
    PoliceOfficerResponse,
    PoliceOfficerListResponse,
    PoliceAlertRequest,
    PoliceActionCreate,
)
from app.services.police_service import PoliceService
from app.core.dependencies import get_current_active_user

router = APIRouter()


@router.get("/officers", response_model=PoliceOfficerListResponse)
async def list_officers(
    rank: Optional[str] = Query(None, description="Filter by rank"),
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=1000),
    current_user: dict = Depends(get_current_active_user),
):
    """List all police officers"""
    service = PoliceService()
    officers = await service.list_officers(rank=rank, skip=skip, limit=limit)
    return officers


@router.post("/alert", status_code=status.HTTP_200_OK)
async def send_police_alert(
    alert_request: PoliceAlertRequest,
    current_user: dict = Depends(get_current_active_user),
):
    """Send alert to police officers"""
    service = PoliceService()
    result = await service.send_alert(
        case_id=alert_request.case_id,
        severity=alert_request.severity,
        num_officers=alert_request.num_officers,
    )
    return result


@router.get("/actions", response_model=List[dict])
async def get_officer_actions(
    case_id: Optional[str] = Query(None, description="Filter by case ID"),
    officer_id: Optional[str] = Query(None, description="Filter by officer ID"),
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=1000),
    current_user: dict = Depends(get_current_active_user),
):
    """Get police officer actions"""
    service = PoliceService()
    actions = await service.get_actions(
        case_id=case_id,
        officer_id=officer_id,
        skip=skip,
        limit=limit,
    )
    return actions


@router.post("/actions", status_code=status.HTTP_201_CREATED)
async def create_officer_action(
    action_data: PoliceActionCreate,
    current_user: dict = Depends(get_current_active_user),
):
    """Create police officer action log"""
    service = PoliceService()
    action = await service.create_action(action_data)
    return action

