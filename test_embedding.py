from utils.embeddings import (
    get_embedding,
    cosine_similarity
)

tcp = get_embedding(
    "TCP provides reliable communication"
)

reliable = get_embedding(
    "How does TCP ensure reliability?"
)

football = get_embedding(
    "Who won the football match?"
)

print(
    cosine_similarity(
        tcp,
        reliable
    )
)

print(
    cosine_similarity(
        tcp,
        football
    )
)