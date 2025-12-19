"""
Decision Orchestrator Agent
Central decision-making hub that coordinates all other agents
"""
from typing import Dict, Any, List, Optional
from loguru import logger
import httpx


class DecisionOrchestratorAgent:
    """Central decision orchestrator agent"""
    
    def __init__(self):
        """Initialize the orchestrator"""
        self.backend_url = "http://localhost:8000"
        self.action_systems_url = "http://localhost:8002"
    
    async def make_decision(self, case_id: str) -> Dict[str, Any]:
        """Make decision for an emergency case"""
        logger.info(f"Making decision for case: {case_id}")
        
        # Fetch case data
        case_data = await self._fetch_case_data(case_id)
        if not case_data:
            return {
                "recommendations": [],
                "confidence": 0.0,
                "reasoning": "Case not found",
                "actions_taken": [],
            }
        
        # Gather all context
        context = await self._gather_context(case_id, case_data)
        
        # Generate recommendations
        recommendations = await self._generate_recommendations(case_id, context)
        
        # Execute actions
        actions_taken = await self._execute_actions(case_id, recommendations)
        
        # Calculate overall confidence
        confidence = self._calculate_confidence(recommendations)
        
        # Generate reasoning
        reasoning = self._generate_reasoning(recommendations, actions_taken)
        
        return {
            "recommendations": recommendations,
            "confidence": confidence,
            "reasoning": reasoning,
            "actions_taken": actions_taken,
        }
    
    async def _fetch_case_data(self, case_id: str) -> Optional[Dict[str, Any]]:
        """Fetch case data from backend"""
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(
                    f"{self.backend_url}/api/v1/emergency/{case_id}"
                )
                if response.status_code == 200:
                    return response.json()
        except Exception as e:
            logger.error(f"Error fetching case data: {e}")
        return None
    
    async def _gather_context(self, case_id: str, case_data: Dict[str, Any]) -> Dict[str, Any]:
        """Gather context from various sources"""
        context = {
            "case_data": case_data,
            "severity": case_data.get("severity_level", "medium"),
            "emergency_type": case_data.get("emergency_type", "other"),
            "location": case_data.get("location", {}),
        }
        
        # Fetch transcript if available
        # Fetch related cases
        # Fetch available resources
        
        return context
    
    async def _generate_recommendations(
        self,
        case_id: str,
        context: Dict[str, Any],
    ) -> List[Dict[str, Any]]:
        """Generate recommendations based on context"""
        recommendations = []
        severity = context.get("severity", "medium")
        emergency_type = context.get("emergency_type", "other")
        
        # Always recommend ambulance for high/critical severity
        if severity in ["high", "critical"]:
            recommendations.append({
                "type": "dispatch_ambulance",
                "priority": 1,
                "confidence": 0.95,
                "reasoning": f"{severity.upper()} severity requires immediate ambulance dispatch",
            })
        
        # Recommend hospital notification for medical emergencies
        if emergency_type == "medical" or severity in ["high", "critical"]:
            recommendations.append({
                "type": "alert_hospital",
                "priority": 2,
                "confidence": 0.9,
                "reasoning": "Medical emergency requires hospital preparation",
            })
        
        # Recommend police for crime/fire/accidents
        if emergency_type in ["crime", "fire", "accident"]:
            recommendations.append({
                "type": "notify_police",
                "priority": 3,
                "confidence": 0.85,
                "reasoning": f"{emergency_type} requires police presence",
            })
        
        # Recommend road clearance for critical cases
        if severity == "critical":
            recommendations.append({
                "type": "request_road_clearance",
                "priority": 4,
                "confidence": 0.8,
                "reasoning": "Critical case may require traffic clearance",
            })
        
        return recommendations
    
    async def _execute_actions(
        self,
        case_id: str,
        recommendations: List[Dict[str, Any]],
    ) -> List[str]:
        """Execute recommended actions"""
        actions_taken = []
        
        for rec in recommendations:
            rec_type = rec.get("type")
            
            try:
                if rec_type == "dispatch_ambulance":
                    # Call ambulance dispatch system
                    await self._dispatch_ambulance(case_id)
                    actions_taken.append("ambulance_dispatched")
                
                elif rec_type == "alert_hospital":
                    # Call hospital notification system
                    await self._alert_hospital(case_id)
                    actions_taken.append("hospital_alerted")
                
                elif rec_type == "notify_police":
                    # Call police alert system
                    await self._notify_police(case_id)
                    actions_taken.append("police_notified")
                
                elif rec_type == "request_road_clearance":
                    # Call road clearance system
                    await self._request_road_clearance(case_id)
                    actions_taken.append("road_clearance_requested")
                    
            except Exception as e:
                logger.error(f"Error executing action {rec_type}: {e}")
        
        return actions_taken
    
    async def _dispatch_ambulance(self, case_id: str):
        """Dispatch ambulance"""
        logger.info(f"Dispatching ambulance for case: {case_id}")
        # In real implementation, call action-systems service
    
    async def _alert_hospital(self, case_id: str):
        """Alert hospital"""
        logger.info(f"Alerting hospital for case: {case_id}")
        # In real implementation, call action-systems service
    
    async def _notify_police(self, case_id: str):
        """Notify police"""
        logger.info(f"Notifying police for case: {case_id}")
        # In real implementation, call action-systems service
    
    async def _request_road_clearance(self, case_id: str):
        """Request road clearance"""
        logger.info(f"Requesting road clearance for case: {case_id}")
        # In real implementation, call action-systems service
    
    def _calculate_confidence(self, recommendations: List[Dict[str, Any]]) -> float:
        """Calculate overall confidence"""
        if not recommendations:
            return 0.0
        
        confidences = [rec.get("confidence", 0.0) for rec in recommendations]
        return sum(confidences) / len(confidences)
    
    def _generate_reasoning(
        self,
        recommendations: List[Dict[str, Any]],
        actions_taken: List[str],
    ) -> str:
        """Generate reasoning text"""
        if not recommendations:
            return "No recommendations generated"
        
        reasoning_parts = []
        for rec in recommendations:
            reasoning_parts.append(rec.get("reasoning", ""))
        
        return " | ".join(reasoning_parts)

