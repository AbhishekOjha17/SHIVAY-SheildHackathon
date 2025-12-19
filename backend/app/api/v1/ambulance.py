"""
Ambulance API endpoints
"""
from fastapi import APIRouter, Depends, HTTPException, status, Query
from typing import List, Optional

from app.schemas.ambulance import (
    AmbulanceResponse,
    AmbulanceListResponse,
    AmbulanceDispatchRequest,
    AmbulanceTrackingUpdate,
)
from app.services.ambulance_service import AmbulanceService
from app.core.dependencies import get_current_active_user

router = APIRouter()


@router.get("/", response_model=AmbulanceListResponse)
async def list_ambulances(
    status: Optional[str] = Query(None, description="Filter by status"),
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=1000),
    current_user: dict = Depends(get_current_active_user),
):
    """List all ambulances"""
    service = AmbulanceService()
    ambulances = await service.list_ambulances(status=status, skip=skip, limit=limit)
    return ambulances


@router.get("/{ambulance_id}", response_model=AmbulanceResponse)
async def get_ambulance(
    ambulance_id: str,
    current_user: dict = Depends(get_current_active_user),
):
    """Get ambulance by ID"""
    service = AmbulanceService()
    ambulance = await service.get_ambulance_by_id(ambulance_id)
    if not ambulance:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Ambulance {ambulance_id} not found",
        )
    return ambulance


@router.get("/{ambulance_id}/tracking", response_model=AmbulanceResponse)
async def get_ambulance_tracking(
    ambulance_id: str,
    current_user: dict = Depends(get_current_active_user),
):
    """Get live tracking data for ambulance"""
    service = AmbulanceService()
    tracking = await service.get_tracking(ambulance_id)
    if not tracking:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Ambulance {ambulance_id} not found",
        )
    return tracking


@router.post("/dispatch", response_model=AmbulanceResponse)
async def dispatch_ambulance(
    dispatch_request: AmbulanceDispatchRequest,
    current_user: dict = Depends(get_current_active_user),
):
    """Dispatch ambulance to emergency case"""
    service = AmbulanceService()
    ambulance = await service.dispatch_ambulance(
        ambulance_id=dispatch_request.ambulance_id,
        case_id=dispatch_request.case_id,
        destination_hospital_id=dispatch_request.destination_hospital_id,
    )
    if not ambulance:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Ambulance {dispatch_request.ambulance_id} not found",
        )
    return ambulance


@router.put("/{ambulance_id}/tracking", response_model=AmbulanceResponse)
async def update_ambulance_tracking(
    ambulance_id: str,
    tracking_update: AmbulanceTrackingUpdate,
    current_user: dict = Depends(get_current_active_user),
):
    """Update ambulance tracking data"""
    service = AmbulanceService()
    ambulance = await service.update_tracking(ambulance_id, tracking_update)
    if not ambulance:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Ambulance {ambulance_id} not found",
        )
    return ambulance

