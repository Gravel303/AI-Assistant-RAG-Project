from utils.embeddings import (
    get_embedding,
    cosine_similarity
)

def fast_semantic_retrieve(
    question,
    chunks,
    chunk_embeddings
):

    question_embedding = (
        get_embedding(question)
    )

    scored_chunks = []

    for chunk, embedding in zip(
        chunks,
        chunk_embeddings
    ):

        score = cosine_similarity(
            question_embedding,
            embedding
        )

        scored_chunks.append(
            (score, chunk)
        )

    scored_chunks.sort(
        reverse=True,
        key=lambda x: x[0]
    )

    return [
        chunk
        for score, chunk
        in scored_chunks[:5]
    ]