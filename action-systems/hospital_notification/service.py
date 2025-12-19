"""
Hospital Notification System
Bed/ICU status, doctor on-call notifications
"""
from typing import Dict, Any, Optional
from loguru import logger
import httpx


class HospitalNotificationService:
    """Service for hospital notifications"""
    
    def __init__(self):
        """Initialize the service"""
        self.backend_url = "http://localhost:8000"
    
    async def notify_hospital(
        self,
        hospital_id: str,
        case_id: str,
        patient_info: Dict[str, Any],
        eta_minutes: Optional[int] = None,
    ) -> Dict[str, Any]:
        """Notify hospital about incoming patient"""
        logger.info(f"Notifying hospital {hospital_id} about case {case_id}")
        
        # Get hospital data
        hospital = await self._get_hospital(hospital_id)
        if not hospital:
            return {
                "success": False,
                "error": "Hospital not found",
            }
        
        # Check resource availability
        resources_available = await self._check_resources(hospital, patient_info)
        
        # Send notification
        notification_sent = await self._send_notification(
            hospital,
            case_id,
            patient_info,
            eta_minutes,
        )
        
        return {
            "success": notification_sent,
            "hospital_id": hospital_id,
            "case_id": case_id,
            "resources_available": resources_available,
            "eta_minutes": eta_minutes,
        }
    
    async def update_hospital_resources(
        self,
        hospital_id: str,
        resources: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Update hospital resource availability"""
        logger.info(f"Updating resources for hospital {hospital_id}")
        
        # In real implementation, update database
        return {
            "success": True,
            "hospital_id": hospital_id,
            "resources": resources,
        }
    
    async def _get_hospital(self, hospital_id: str) -> Optional[Dict[str, Any]]:
        """Get hospital data"""
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(
                    f"{self.backend_url}/api/v1/hospital/{hospital_id}"
                )
                if response.status_code == 200:
                    return response.json()
        except Exception as e:
            logger.error(f"Error fetching hospital: {e}")
        return None
    
    async def _check_resources(
        self,
        hospital: Dict[str, Any],
        patient_info: Dict[str, Any],
    ) -> bool:
        """Check if hospital has required resources"""
        severity = patient_info.get("severity", "medium")
        
        # Check ICU availability for critical cases
        if severity == "critical":
            icu_available = hospital.get("icu_available", 0)
            return icu_available > 0
        
        # Check bed availability for other cases
        beds_available = hospital.get("available_beds", 0)
        return beds_available > 0
    
    async def _send_notification(
        self,
        hospital: Dict[str, Any],
        case_id: str,
        patient_info: Dict[str, Any],
        eta_minutes: Optional[int],
    ) -> bool:
        """Send notification to hospital"""
        # In real implementation, send SMS/call/email to hospital
        doctor_phone = hospital.get("doctor_phone")
        emergency_phone = hospital.get("emergency_phone")
        
        if doctor_phone or emergency_phone:
            # Send notification via communication service
            logger.info(f"Notification sent to hospital {hospital.get('hospital_id')}")
            return True
        
        return False

