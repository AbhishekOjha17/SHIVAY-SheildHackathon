"""
Case Clustering Agent
Detects similar cases using vector embeddings
"""
from typing import Dict, Any, List, Optional
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from loguru import logger


class CaseClusteringAgent:
    """Agent for case clustering"""
    
    def __init__(self):
        """Initialize the agent"""
        self.sentence_model = None
        self.similarity_threshold = 0.75
        self._load_model()
    
    def _load_model(self):
        """Load sentence transformer model"""
        try:
            logger.info("Loading sentence transformer model...")
            self.sentence_model = SentenceTransformer('all-MiniLM-L6-v2')
            logger.info("Sentence transformer model loaded")
        except Exception as e:
            logger.error(f"Failed to load model: {e}")
    
    async def find_similar_cases(
        self,
        case_id: str,
        case_text: str,
        historical_cases: List[Dict[str, Any]],
    ) -> Dict[str, Any]:
        """Find similar cases using vector embeddings"""
        logger.info(f"Finding similar cases for case: {case_id}")
        
        if not self.sentence_model or not historical_cases:
            return {
                "related_cases": [],
                "similarity_scores": {},
                "cluster_id": None,
            }
        
        try:
            # Generate embedding for current case
            current_embedding = self.sentence_model.encode(case_text)
            
            # Generate embeddings for historical cases
            historical_texts = [
                self._extract_case_text(case) for case in historical_cases
            ]
            historical_embeddings = self.sentence_model.encode(historical_texts)
            
            # Calculate similarities
            similarities = cosine_similarity(
                [current_embedding],
                historical_embeddings
            )[0]
            
            # Find similar cases (above threshold)
            similar_cases = []
            similarity_scores = {}
            
            for i, similarity in enumerate(similarities):
                if similarity >= self.similarity_threshold:
                    case = historical_cases[i]
                    case_id_hist = case.get("case_id", f"case_{i}")
                    similar_cases.append(case_id_hist)
                    similarity_scores[case_id_hist] = float(similarity)
            
            # Sort by similarity
            similar_cases = sorted(
                similar_cases,
                key=lambda x: similarity_scores[x],
                reverse=True
            )[:10]  # Top 10 similar cases
            
            return {
                "related_cases": similar_cases,
                "similarity_scores": {
                    k: v for k, v in similarity_scores.items()
                    if k in similar_cases
                },
                "cluster_id": self._generate_cluster_id(case_id, similar_cases),
            }
            
        except Exception as e:
            logger.error(f"Error finding similar cases: {e}")
            return {
                "related_cases": [],
                "similarity_scores": {},
                "cluster_id": None,
            }
    
    def _extract_case_text(self, case: Dict[str, Any]) -> str:
        """Extract text representation of case for embedding"""
        parts = []
        
        if case.get("description"):
            parts.append(case["description"])
        
        if case.get("emergency_type"):
            parts.append(f"Type: {case['emergency_type']}")
        
        if case.get("location_address"):
            parts.append(f"Location: {case['location_address']}")
        
        return " ".join(parts) if parts else "Emergency case"
    
    def _generate_cluster_id(self, case_id: str, similar_cases: List[str]) -> Optional[str]:
        """Generate cluster ID if multiple similar cases found"""
        if len(similar_cases) >= 2:
            return f"CLUSTER-{case_id[:8]}"
        return None
    
    async def cluster_cases(self, cases: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Cluster multiple cases together"""
        if not self.sentence_model or len(cases) < 2:
            return {
                "clusters": [],
                "cluster_assignments": {},
            }
        
        try:
            # Generate embeddings
            case_texts = [self._extract_case_text(case) for case in cases]
            embeddings = self.sentence_model.encode(case_texts)
            
            # Simple clustering based on similarity
            clusters = []
            cluster_assignments = {}
            used = set()
            
            for i, case in enumerate(cases):
                if i in used:
                    continue
                
                cluster = [i]
                used.add(i)
                
                for j in range(i + 1, len(cases)):
                    if j in used:
                        continue
                    
                    similarity = cosine_similarity(
                        [embeddings[i]],
                        [embeddings[j]]
                    )[0][0]
                    
                    if similarity >= self.similarity_threshold:
                        cluster.append(j)
                        used.add(j)
                
                if len(cluster) > 1:
                    cluster_id = f"CLUSTER-{cases[cluster[0]]['case_id'][:8]}"
                    clusters.append({
                        "cluster_id": cluster_id,
                        "case_ids": [cases[idx]["case_id"] for idx in cluster],
                    })
                    
                    for idx in cluster:
                        cluster_assignments[cases[idx]["case_id"]] = cluster_id
            
            return {
                "clusters": clusters,
                "cluster_assignments": cluster_assignments,
            }
            
        except Exception as e:
            logger.error(f"Error clustering cases: {e}")
            return {
                "clusters": [],
                "cluster_assignments": {},
            }

