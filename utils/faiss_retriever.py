import numpy as np

from utils.embeddings import (
    get_embedding
)

def faiss_retrieve(
    question,
    index,
    chunks,
    top_k=5
):

    question_embedding = (
        get_embedding(question)
    )

    question_embedding = np.array(
        [question_embedding],
        dtype=np.float32
    )

    distances, indices = index.search(
        question_embedding,
        top_k
    )

    relevant_chunks = []

    for idx in indices[0]:

        relevant_chunks.append(
            chunks[idx]
        )

    return relevant_chunks