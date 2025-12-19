"""
AI agent schemas
"""
from pydantic import BaseModel
from typing import Optional, Dict, Any, List


class TranscriptionRequest(BaseModel):
    """Schema for transcription request"""
    audio_url: str
    language: Optional[str] = None


class TranscriptionResponse(BaseModel):
    """Schema for transcription response"""
    transcript: str
    language: str
    confidence: float
    duration: Optional[float] = None


class NLPAnalysisRequest(BaseModel):
    """Schema for NLP analysis request"""
    text: str
    case_id: Optional[str] = None


class NLPAnalysisResponse(BaseModel):
    """Schema for NLP analysis response"""
    intent: str
    entities: Dict[str, Any]
    urgency_score: float
    extracted_location: Optional[Dict[str, Any]] = None
    extracted_people_count: Optional[int] = None


class SeverityScoringRequest(BaseModel):
    """Schema for severity scoring request"""
    case_id: str
    context: Optional[Dict[str, Any]] = None


class SeverityScoringResponse(BaseModel):
    """Schema for severity scoring response"""
    severity_level: str
    severity_score: float
    confidence: float
    reasoning: Optional[str] = None


class CaseClusteringRequest(BaseModel):
    """Schema for case clustering request"""
    case_id: str


class CaseClusteringResponse(BaseModel):
    """Schema for case clustering response"""
    related_cases: List[str]
    similarity_scores: Dict[str, float]
    cluster_id: Optional[str] = None


class DecisionRequest(BaseModel):
    """Schema for decision request"""
    case_id: str


class DecisionResponse(BaseModel):
    """Schema for decision response"""
    recommendations: List[Dict[str, Any]]
    confidence: float
    reasoning: str
    actions_taken: List[str] = []

