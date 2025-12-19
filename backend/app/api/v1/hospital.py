"""
Hospital API endpoints
"""
from fastapi import APIRouter, Depends, HTTPException, status, Query
from typing import List, Optional

from app.schemas.hospital import (
    HospitalResponse,
    HospitalListResponse,
    HospitalResourceUpdate,
)
from app.services.hospital_service import HospitalService
from app.core.dependencies import get_current_active_user

router = APIRouter()


@router.get("/", response_model=HospitalListResponse)
async def list_hospitals(
    is_active: Optional[bool] = Query(None, description="Filter by active status"),
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=1000),
    current_user: dict = Depends(get_current_active_user),
):
    """List all hospitals"""
    service = HospitalService()
    hospitals = await service.list_hospitals(is_active=is_active, skip=skip, limit=limit)
    return hospitals


@router.get("/{hospital_id}", response_model=HospitalResponse)
async def get_hospital(
    hospital_id: str,
    current_user: dict = Depends(get_current_active_user),
):
    """Get hospital by ID"""
    service = HospitalService()
    hospital = await service.get_hospital_by_id(hospital_id)
    if not hospital:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Hospital {hospital_id} not found",
        )
    return hospital


@router.get("/{hospital_id}/resources", response_model=HospitalResponse)
async def get_hospital_resources(
    hospital_id: str,
    current_user: dict = Depends(get_current_active_user),
):
    """Get hospital resource availability"""
    service = HospitalService()
    hospital = await service.get_hospital_by_id(hospital_id)
    if not hospital:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Hospital {hospital_id} not found",
        )
    return hospital


@router.put("/{hospital_id}/resources", response_model=HospitalResponse)
async def update_hospital_resources(
    hospital_id: str,
    resource_update: HospitalResourceUpdate,
    current_user: dict = Depends(get_current_active_user),
):
    """Update hospital resource availability"""
    service = HospitalService()
    hospital = await service.update_resources(hospital_id, resource_update)
    if not hospital:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Hospital {hospital_id} not found",
        )
    return hospital

