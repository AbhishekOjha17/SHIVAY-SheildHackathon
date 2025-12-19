"""
AI Agent API endpoints
"""
from fastapi import APIRouter, Depends, HTTPException, status, File, UploadFile
from typing import Optional

from app.schemas.ai import (
    TranscriptionRequest,
    TranscriptionResponse,
    NLPAnalysisRequest,
    NLPAnalysisResponse,
    SeverityScoringRequest,
    SeverityScoringResponse,
    CaseClusteringRequest,
    CaseClusteringResponse,
    DecisionRequest,
    DecisionResponse,
)
from app.services.ai_service import AIService
from app.core.dependencies import get_current_active_user

router = APIRouter()


@router.post("/transcribe", response_model=TranscriptionResponse)
async def transcribe_audio(
    request: TranscriptionRequest,
    current_user: dict = Depends(get_current_active_user),
):
    """Transcribe audio using Speech-to-Text agent"""
    service = AIService()
    result = await service.transcribe_audio(
        audio_url=request.audio_url,
        language=request.language,
    )
    return result


@router.post("/analyze", response_model=NLPAnalysisResponse)
async def analyze_text(
    request: NLPAnalysisRequest,
    current_user: dict = Depends(get_current_active_user),
):
    """Analyze text using NLP Understanding agent"""
    service = AIService()
    result = await service.analyze_text(
        text=request.text,
        case_id=request.case_id,
    )
    return result


@router.post("/severity", response_model=SeverityScoringResponse)
async def score_severity(
    request: SeverityScoringRequest,
    current_user: dict = Depends(get_current_active_user),
):
    """Score severity using Severity Scoring agent"""
    service = AIService()
    result = await service.score_severity(
        case_id=request.case_id,
        context=request.context,
    )
    return result


@router.post("/cluster", response_model=CaseClusteringResponse)
async def cluster_cases(
    request: CaseClusteringRequest,
    current_user: dict = Depends(get_current_active_user),
):
    """Cluster similar cases using Case Clustering agent"""
    service = AIService()
    result = await service.cluster_cases(
        case_id=request.case_id,
    )
    return result


@router.post("/decide", response_model=DecisionResponse)
async def make_decision(
    request: DecisionRequest,
    current_user: dict = Depends(get_current_active_user),
):
    """Make decision using Decision Orchestrator agent"""
    service = AIService()
    result = await service.make_decision(
        case_id=request.case_id,
    )
    return result

