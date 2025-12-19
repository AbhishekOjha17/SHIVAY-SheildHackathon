"""
Speech-to-Text Agent
Converts emergency call audio to text using Whisper/DeepSpeech
"""
import whisper
import os
from typing import Optional, Dict, Any
from loguru import logger
import httpx


class SpeechToTextAgent:
    """Agent for speech-to-text conversion"""
    
    def __init__(self, model_name: str = "base"):
        """Initialize the agent with a model"""
        self.model_name = model_name
        self.model = None
        self._load_model()
    
    def _load_model(self):
        """Load the Whisper model"""
        try:
            logger.info(f"Loading Whisper model: {self.model_name}")
            self.model = whisper.load_model(self.model_name)
            logger.info("Whisper model loaded successfully")
        except Exception as e:
            logger.error(f"Failed to load Whisper model: {e}")
            self.model = None
    
    async def transcribe_from_url(self, audio_url: str, language: Optional[str] = None) -> Dict[str, Any]:
        """Transcribe audio from URL"""
        try:
            # Download audio file
            async with httpx.AsyncClient() as client:
                response = await client.get(audio_url)
                audio_data = response.content
            
            # Save temporarily
            temp_file = "/tmp/audio_temp.wav"
            with open(temp_file, "wb") as f:
                f.write(audio_data)
            
            # Transcribe
            result = await self.transcribe_from_file(temp_file, language)
            
            # Clean up
            if os.path.exists(temp_file):
                os.remove(temp_file)
            
            return result
            
        except Exception as e:
            logger.error(f"Error transcribing from URL: {e}")
            return {
                "transcript": "",
                "language": language or "en",
                "confidence": 0.0,
                "error": str(e),
            }
    
    async def transcribe_from_file(self, audio_file: str, language: Optional[str] = None) -> Dict[str, Any]:
        """Transcribe audio from file"""
        if not self.model:
            return {
                "transcript": "",
                "language": language or "en",
                "confidence": 0.0,
                "error": "Model not loaded",
            }
        
        try:
            logger.info(f"Transcribing audio file: {audio_file}")
            
            # Transcribe with Whisper
            result = self.model.transcribe(
                audio_file,
                language=language,
                task="transcribe",
            )
            
            transcript = result["text"]
            detected_language = result.get("language", language or "en")
            
            # Calculate average confidence (Whisper doesn't provide this directly)
            # Using segment-level confidence if available
            segments = result.get("segments", [])
            if segments:
                avg_confidence = sum(s.get("no_speech_prob", 0) for s in segments) / len(segments)
                confidence = 1.0 - avg_confidence  # Invert no_speech_prob
            else:
                confidence = 0.9  # Default confidence
            
            logger.info(f"Transcription completed. Language: {detected_language}, Confidence: {confidence:.2f}")
            
            return {
                "transcript": transcript,
                "language": detected_language,
                "confidence": confidence,
                "duration": result.get("duration", 0),
            }
            
        except Exception as e:
            logger.error(f"Error transcribing audio: {e}")
            return {
                "transcript": "",
                "language": language or "en",
                "confidence": 0.0,
                "error": str(e),
            }
    
    async def process_call_recording(self, call_id: str, audio_url: str) -> Dict[str, Any]:
        """Process call recording for a specific case"""
        logger.info(f"Processing call recording for call: {call_id}")
        
        result = await self.transcribe_from_url(audio_url)
        result["call_id"] = call_id
        
        return result

