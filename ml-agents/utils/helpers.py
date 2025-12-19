"""
Helper utilities for ML agents
"""
from typing import List, Dict, Any
import numpy as np


def normalize_embeddings(embeddings: List[float]) -> List[float]:
    """Normalize embeddings to unit vector"""
    arr = np.array(embeddings)
    norm = np.linalg.norm(arr)
    if norm > 0:
        return (arr / norm).tolist()
    return embeddings


def calculate_similarity(emb1: List[float], emb2: List[float]) -> float:
    """Calculate cosine similarity between embeddings"""
    arr1 = np.array(emb1)
    arr2 = np.array(emb2)
    
    dot_product = np.dot(arr1, arr2)
    norm1 = np.linalg.norm(arr1)
    norm2 = np.linalg.norm(arr2)
    
    if norm1 > 0 and norm2 > 0:
        return float(dot_product / (norm1 * norm2))
    return 0.0

