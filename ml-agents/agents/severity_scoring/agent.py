"""
Severity Scoring Agent
Assigns severity levels (Critical/High/Med/Low) to emergency cases
"""
from typing import Dict, Any, Optional
from enum import Enum
from loguru import logger
from sklearn.ensemble import RandomForestClassifier
import numpy as np


class SeverityLevel(str, Enum):
    """Severity levels"""
    CRITICAL = "critical"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"


class SeverityScoringAgent:
    """Agent for severity scoring"""
    
    def __init__(self):
        """Initialize the agent"""
        self.model = None
        self._initialize_model()
    
    def _initialize_model(self):
        """Initialize severity scoring model"""
        # In a real implementation, this would load a trained model
        # For now, we use rule-based scoring with ML fallback
        try:
            self.model = RandomForestClassifier(n_estimators=100, random_state=42)
            # Model would be trained on historical data
            logger.info("Severity scoring model initialized")
        except Exception as e:
            logger.error(f"Failed to initialize model: {e}")
    
    async def score_severity(
        self,
        case_id: str,
        context: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Score severity for an emergency case"""
        logger.info(f"Scoring severity for case: {case_id}")
        
        if not context:
            context = {}
        
        # Extract features
        features = self._extract_features(context)
        
        # Calculate severity score
        severity_score = self._calculate_severity_score(features)
        
        # Determine severity level
        severity_level = self._determine_severity_level(severity_score)
        
        # Generate reasoning
        reasoning = self._generate_reasoning(features, severity_level)
        
        return {
            "severity_level": severity_level.value,
            "severity_score": severity_score,
            "confidence": 0.85,  # Would be calculated from model
            "reasoning": reasoning,
        }
    
    def _extract_features(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """Extract features from context"""
        features = {
            "urgency_score": context.get("urgency_score", 0.5),
            "people_involved": context.get("people_involved", 1),
            "injuries_reported": context.get("injuries_reported", 0),
            "emergency_type": context.get("emergency_type", "other"),
            "has_keywords": self._check_critical_keywords(context.get("description", "")),
            "call_duration": context.get("call_duration", 0),
        }
        return features
    
    def _check_critical_keywords(self, text: str) -> bool:
        """Check for critical keywords"""
        if not text:
            return False
        
        critical_keywords = [
            "unconscious", "not breathing", "cardiac arrest",
            "severe bleeding", "fire", "explosion", "multiple injuries",
            "trapped", "critical condition",
        ]
        
        text_lower = text.lower()
        return any(keyword in text_lower for keyword in critical_keywords)
    
    def _calculate_severity_score(self, features: Dict[str, Any]) -> float:
        """Calculate severity score (0-1)"""
        score = 0.0
        
        # Urgency score contribution (40%)
        score += features["urgency_score"] * 0.4
        
        # People involved (20%)
        people_factor = min(1.0, features["people_involved"] / 5.0)
        score += people_factor * 0.2
        
        # Injuries reported (20%)
        injuries_factor = min(1.0, features["injuries_reported"] / 3.0)
        score += injuries_factor * 0.2
        
        # Critical keywords (10%)
        if features["has_keywords"]:
            score += 0.1
        
        # Emergency type (10%)
        type_scores = {
            "medical": 0.8,
            "accident": 0.7,
            "fire": 0.9,
            "crime": 0.6,
            "natural_disaster": 0.85,
            "other": 0.5,
        }
        type_score = type_scores.get(features["emergency_type"], 0.5)
        score += type_score * 0.1
        
        return min(1.0, score)
    
    def _determine_severity_level(self, severity_score: float) -> SeverityLevel:
        """Determine severity level from score"""
        if severity_score >= 0.85:
            return SeverityLevel.CRITICAL
        elif severity_score >= 0.65:
            return SeverityLevel.HIGH
        elif severity_score >= 0.4:
            return SeverityLevel.MEDIUM
        else:
            return SeverityLevel.LOW
    
    def _generate_reasoning(self, features: Dict[str, Any], severity_level: SeverityLevel) -> str:
        """Generate reasoning for severity level"""
        reasons = []
        
        if features["urgency_score"] > 0.8:
            reasons.append("High urgency reported")
        
        if features["people_involved"] > 1:
            reasons.append(f"{features['people_involved']} people involved")
        
        if features["injuries_reported"] > 0:
            reasons.append(f"{features['injuries_reported']} injuries reported")
        
        if features["has_keywords"]:
            reasons.append("Critical keywords detected")
        
        if not reasons:
            reasons.append("Standard emergency case")
        
        return f"{severity_level.value.upper()} severity: " + ", ".join(reasons)

