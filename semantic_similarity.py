# semantic_similarity.py

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load once (important for performance)
model = SentenceTransformer("all-MiniLM-L6-v2")


def compute_similarity(resume_text: str, job_description: str) -> float:
    """
    Returns cosine similarity between resume and job description
    Value range: 0 → 1
    """
    embeddings = model.encode([resume_text, job_description])
    score = cosine_similarity(
        [embeddings[0]],
        [embeddings[1]]
    )[0][0]

    return round(float(score), 3)
