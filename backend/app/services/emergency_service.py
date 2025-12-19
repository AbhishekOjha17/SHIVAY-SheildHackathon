"""
Emergency case service
"""
from typing import Optional, List
from datetime import datetime
import uuid

from app.models.emergency import EmergencyCase, EmergencyStatus, SeverityLevel, EmergencyType
from app.schemas.emergency import EmergencyCaseCreate, EmergencyCaseUpdate
from loguru import logger


class EmergencyService:
    """Service for emergency case operations"""
    
    async def create_case(self, case_data: EmergencyCaseCreate) -> EmergencyCase:
        """Create a new emergency case"""
        case_id = f"CASE-{uuid.uuid4().hex[:8].upper()}"
        
        case = EmergencyCase(
            case_id=case_id,
            **case_data.dict(),
        )
        
        await case.insert()
        logger.info(f"Created emergency case: {case_id}")
        return case
    
    async def get_case_by_id(self, case_id: str) -> Optional[EmergencyCase]:
        """Get emergency case by ID"""
        return await EmergencyCase.find_one(EmergencyCase.case_id == case_id)
    
    async def list_cases(
        self,
        status: Optional[EmergencyStatus] = None,
        severity: Optional[SeverityLevel] = None,
        emergency_type: Optional[EmergencyType] = None,
        skip: int = 0,
        limit: int = 100,
    ) -> dict:
        """List emergency cases with filters"""
        query = {}
        
        if status:
            query["status"] = status
        if severity:
            query["severity_level"] = severity
        if emergency_type:
            query["emergency_type"] = emergency_type
        
        cases = await EmergencyCase.find(query).skip(skip).limit(limit).to_list()
        total = await EmergencyCase.find(query).count()
        
        return {
            "cases": cases,
            "total": total,
            "skip": skip,
            "limit": limit,
        }
    
    async def update_case(
        self,
        case_id: str,
        case_data: EmergencyCaseUpdate,
    ) -> Optional[EmergencyCase]:
        """Update emergency case"""
        case = await self.get_case_by_id(case_id)
        if not case:
            return None
        
        update_data = case_data.dict(exclude_unset=True)
        update_data["updated_at"] = datetime.utcnow()
        
        for key, value in update_data.items():
            setattr(case, key, value)
        
        await case.save()
        logger.info(f"Updated emergency case: {case_id}")
        return case
    
    async def delete_case(self, case_id: str) -> bool:
        """Delete emergency case"""
        case = await self.get_case_by_id(case_id)
        if not case:
            return False
        
        await case.delete()
        logger.info(f"Deleted emergency case: {case_id}")
        return True
    
    async def resolve_case(self, case_id: str) -> Optional[EmergencyCase]:
        """Mark emergency case as resolved"""
        case = await self.get_case_by_id(case_id)
        if not case:
            return None
        
        case.status = EmergencyStatus.RESOLVED
        case.resolved_at = datetime.utcnow()
        case.updated_at = datetime.utcnow()
        
        await case.save()
        logger.info(f"Resolved emergency case: {case_id}")
        return case

