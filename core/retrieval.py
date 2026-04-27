import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from config.settings import model

def retrieve_context(question, documents, top_k=3):
    query_embedding = model.encode([question])

    all_chunks = []
    all_embeddings = []

    for doc in documents:
        all_chunks.extend(doc["chunks"])
        all_embeddings.extend(doc["embeddings"])

    if not all_chunks:
        return ""

    sims = cosine_similarity(query_embedding, all_embeddings)[0]
    top_indices = np.argsort(sims)[-top_k:][::-1]

    selected_chunks = [all_chunks[i] for i in top_indices]
    return "\n".join(selected_chunks)