"""
NLP Understanding Agent
Extracts intent, entities, and urgency from text
"""
from typing import Dict, Any, Optional, List
from sentence_transformers import SentenceTransformer
from transformers import pipeline
import spacy
from loguru import logger


class NLPUnderstandingAgent:
    """Agent for NLP understanding"""
    
    def __init__(self):
        """Initialize the agent"""
        self.intent_classifier = None
        self.ner_model = None
        self.urgency_classifier = None
        self.sentence_model = None
        self._load_models()
    
    def _load_models(self):
        """Load NLP models"""
        try:
            logger.info("Loading NLP models...")
            
            # Intent classification
            self.intent_classifier = pipeline(
                "zero-shot-classification",
                model="facebook/bart-large-mnli",
            )
            
            # Named Entity Recognition
            try:
                self.ner_model = spacy.load("en_core_web_sm")
            except OSError:
                logger.warning("spaCy model not found. Install with: python -m spacy download en_core_web_sm")
                self.ner_model = None
            
            # Sentence transformer for embeddings
            self.sentence_model = SentenceTransformer('all-MiniLM-L6-v2')
            
            logger.info("NLP models loaded successfully")
            
        except Exception as e:
            logger.error(f"Failed to load NLP models: {e}")
    
    async def analyze_text(self, text: str, case_id: Optional[str] = None) -> Dict[str, Any]:
        """Analyze text for intent, entities, and urgency"""
        if not text:
            return {
                "intent": "unknown",
                "entities": {},
                "urgency_score": 0.0,
                "extracted_location": None,
                "extracted_people_count": None,
            }
        
        logger.info(f"Analyzing text for case: {case_id}")
        
        # Extract intent
        intent = await self._extract_intent(text)
        
        # Extract entities
        entities = await self._extract_entities(text)
        
        # Calculate urgency score
        urgency_score = await self._calculate_urgency(text, entities)
        
        # Extract location
        location = self._extract_location(entities)
        
        # Extract people count
        people_count = self._extract_people_count(text, entities)
        
        return {
            "intent": intent,
            "entities": entities,
            "urgency_score": urgency_score,
            "extracted_location": location,
            "extracted_people_count": people_count,
        }
    
    async def _extract_intent(self, text: str) -> str:
        """Extract intent from text"""
        if not self.intent_classifier:
            return "unknown"
        
        intent_labels = [
            "medical_emergency",
            "accident",
            "fire",
            "crime",
            "natural_disaster",
            "other",
        ]
        
        try:
            result = self.intent_classifier(text, intent_labels)
            return result["labels"][0] if result["labels"] else "unknown"
        except Exception as e:
            logger.error(f"Error extracting intent: {e}")
            return "unknown"
    
    async def _extract_entities(self, text: str) -> Dict[str, Any]:
        """Extract named entities from text"""
        entities = {
            "locations": [],
            "people": [],
            "organizations": [],
            "dates": [],
            "numbers": [],
        }
        
        if self.ner_model:
            try:
                doc = self.ner_model(text)
                for ent in doc.ents:
                    if ent.label_ == "GPE" or ent.label_ == "LOC":
                        entities["locations"].append(ent.text)
                    elif ent.label_ == "PERSON":
                        entities["people"].append(ent.text)
                    elif ent.label_ == "ORG":
                        entities["organizations"].append(ent.text)
                    elif ent.label_ == "DATE":
                        entities["dates"].append(ent.text)
                    elif ent.label_ == "CARDINAL":
                        entities["numbers"].append(ent.text)
            except Exception as e:
                logger.error(f"Error extracting entities: {e}")
        
        return entities
    
    async def _calculate_urgency(self, text: str, entities: Dict[str, Any]) -> float:
        """Calculate urgency score (0-1)"""
        urgency_keywords = {
            "critical": 1.0,
            "urgent": 0.9,
            "emergency": 0.9,
            "immediate": 0.85,
            "serious": 0.8,
            "severe": 0.8,
            "bleeding": 0.75,
            "unconscious": 0.9,
            "not breathing": 0.95,
            "fire": 0.85,
            "explosion": 0.9,
            "accident": 0.7,
        }
        
        text_lower = text.lower()
        max_score = 0.5  # Base urgency
        
        for keyword, score in urgency_keywords.items():
            if keyword in text_lower:
                max_score = max(max_score, score)
        
        # Increase urgency if multiple people involved
        numbers = entities.get("numbers", [])
        if numbers:
            try:
                people_count = sum(int(n) for n in numbers if n.isdigit())
                if people_count > 1:
                    max_score = min(1.0, max_score + 0.1)
            except:
                pass
        
        return min(1.0, max_score)
    
    def _extract_location(self, entities: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """Extract location from entities"""
        locations = entities.get("locations", [])
        if locations:
            return {
                "name": locations[0],
                "type": "address",
            }
        return None
    
    def _extract_people_count(self, text: str, entities: Dict[str, Any]) -> Optional[int]:
        """Extract people count from text"""
        import re
        
        # Look for numbers in text
        numbers = re.findall(r'\d+', text)
        if numbers:
            try:
                return int(numbers[0])
            except:
                pass
        
        # Check entities
        entity_numbers = entities.get("numbers", [])
        if entity_numbers:
            try:
                return int(entity_numbers[0])
            except:
                pass
        
        return None
    
    def get_text_embedding(self, text: str) -> List[float]:
        """Get text embedding for clustering"""
        if not self.sentence_model:
            return []
        
        try:
            embedding = self.sentence_model.encode(text)
            return embedding.tolist()
        except Exception as e:
            logger.error(f"Error generating embedding: {e}")
            return []

