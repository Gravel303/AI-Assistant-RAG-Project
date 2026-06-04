def retrieve_chunks(question, chunks):

    stop_words = {
    "what",
    "is",
    "the",
    "a",
    "an",
    "of",
    "in",
    "to",
    "for"
    }

    question_words = [
        word for word in question.lower().split()
        if word not in stop_words
    ]

    scored_chunks = []

    for chunk in chunks:

        score = 0

        chunk_lower = chunk.lower()

        for word in question_words:

            if word in chunk_lower:
                score += 1

        scored_chunks.append((score, chunk))

    scored_chunks.sort(
        reverse=True,
        key=lambda x: x[0]
    )

    return [
        chunk
        for score, chunk in scored_chunks[:5]
    ]