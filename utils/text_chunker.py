def chunk_text(
    pages,
    chunk_size=1000,
    overlap=200
):

    chunks = []

    # print(
    # "chunk_text called",
    # len(pages)
    # )

    for page_data in pages:

        # print(
        # "processing page",
        # page_data["page"]
        # )

        page_number = page_data["page"]

        text = page_data["text"]

        start = 0

        while start < len(text):

            end = start + chunk_size

            chunk = text[start:end]

            chunks.append(
                {
                    "text": chunk,
                    "page": page_number
                }
            )

            start += (
                chunk_size - overlap
            )
    # print(
    # "returning",
    # len(chunks),
    # "chunks"
    # )
    return chunks