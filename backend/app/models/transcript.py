"""
Caller Transcript Model
"""
from beanie import Document
from pydantic import Field
from typing import Optional, Dict, Any, List
from datetime import datetime
from enum import Enum


class TranscriptStatus(str, Enum):
    """Transcript processing status"""
    PENDING = "pending"
    PROCESSING = "processing"
    COMPLETED = "completed"
    FAILED = "failed"


class CallerTranscript(Document):
    """Caller transcript document"""
    
    case_id: str = Field(..., description="Associated emergency case ID")
    call_id: Optional[str] = Field(None, description="Call identifier from Twilio/Exotel")
    
    raw_audio_url: Optional[str] = Field(None, description="URL to raw audio file in Cloudinary")
    audio_duration: Optional[float] = Field(None, description="Audio duration in seconds")
    
    transcript_text: Optional[str] = Field(None, description="Transcribed text")
    transcript_status: TranscriptStatus = Field(
        default=TranscriptStatus.PENDING,
        description="Processing status"
    )
    
    extracted_entities: Dict[str, Any] = Field(
        default_factory=dict,
        description="Extracted named entities"
    )
    intent: Optional[str] = Field(None, description="Detected intent")
    urgency_score: Optional[float] = Field(None, description="Urgency score (0-1)")
    
    language: Optional[str] = Field(None, description="Detected language")
    confidence: Optional[float] = Field(None, description="Transcription confidence")
    
    processing_errors: List[str] = Field(default_factory=list, description="Processing errors")
    
    created_at: datetime = Field(default_factory=datetime.utcnow, description="Creation timestamp")
    processed_at: Optional[datetime] = Field(None, description="Processing completion timestamp")
    
    metadata: Dict[str, Any] = Field(default_factory=dict, description="Additional metadata")
    
    class Settings:
        name = "Caller_Transcripts"
        indexes = [
            "case_id",
            "call_id",
            "transcript_status",
            "created_at",
        ]

