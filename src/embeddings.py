"""
Embedding generation using OpenAI's text-embedding-3-small model.
"""
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

_client = None


def get_client():
    """Get or create OpenAI client singleton."""
    global _client
    if _client is None:
        _client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    return _client


def get_embedding(text: str, model: str = "text-embedding-3-small") -> list[float]:
    """Get embedding vector for a single text string."""
    client = get_client()
    response = client.embeddings.create(input=text, model=model)
    return response.data[0].embedding


def get_embeddings(texts: list[str], model: str = "text-embedding-3-small") -> list[list[float]]:
    """Get embedding vectors for multiple texts in a single API call."""
    if not texts:
        return []
    client = get_client()
    response = client.embeddings.create(input=texts, model=model)
    return [item.embedding for item in response.data]


def cosine_similarity(v1: list[float], v2: list[float]) -> float:
    """Calculate cosine similarity between two vectors."""
    import numpy as np
    v1, v2 = np.array(v1), np.array(v2)
    return float(np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2)))


def euclidean_distance(v1: list[float], v2: list[float]) -> float:
    """Calculate Euclidean distance between two vectors."""
    import numpy as np
    return float(np.linalg.norm(np.array(v1) - np.array(v2)))
