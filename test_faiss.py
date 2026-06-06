from utils.embeddings import (
    get_embedding
)

from utils.faiss_manager import (
    build_faiss_index
)

embeddings = []

embeddings.append(
    get_embedding(
        "TCP provides reliable communication"
    )
)

embeddings.append(
    get_embedding(
        "Football is a popular sport"
    )
)

index = build_faiss_index(
    embeddings
)
print(type(index))
print(index.ntotal)