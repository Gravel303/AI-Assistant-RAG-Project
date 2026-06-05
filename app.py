import streamlit as st

from utils.fast_semantic_retriever import fast_semantic_retrieve
# from utils.retriever import retrieve_chunks

from utils.text_chunker import chunk_text

from utils.gemini_client import ask_gemini

from utils.pdf_processor import extract_text_from_pdf

from utils.embeddings import get_embedding

st.set_page_config(
    page_title="AI Study Assistant",
    page_icon="📚"
)

st.title("📚 AI Study Assistant")

if "current_pdf" not in st.session_state:
    st.session_state.current_pdf = None

uploaded_file = st.file_uploader(
    "Upload a PDF",
    type="pdf"
)

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])


question = st.chat_input(
    "Ask a study question..."
)

if "chunks" not in st.session_state:
    st.session_state.chunks = []

if "chunk_embeddings" not in st.session_state:
    st.session_state.chunk_embeddings = []

if (
    uploaded_file
    and uploaded_file.name
    != st.session_state.current_pdf
):
    if not st.session_state.chunk_embeddings:
        pdf_text = extract_text_from_pdf(
            uploaded_file
        )

        chunks = chunk_text(pdf_text)

        chunk_embeddings = []

        with st.spinner(
            "Generating embeddings..."
        ):

            for chunk in chunks:

                embedding = get_embedding(
                    chunk
                )

                chunk_embeddings.append(
                    embedding
                )
        st.write(
        f"Stored {len(chunk_embeddings)} embeddings"
        )

        st.session_state.chunks = chunks

        st.session_state.chunk_embeddings = (
            chunk_embeddings
        )

        st.session_state.current_pdf = (
            uploaded_file.name
        )

        st.success("PDF loaded!")

        st.text_area(
        "PDF Preview",
        pdf_text[:3000],
        height=300
        )  





if question:

    if uploaded_file:

        relevant_chunks = fast_semantic_retrieve(
        question,
        st.session_state.chunks,
        st.session_state.chunk_embeddings
        )

        context = "\n\n".join(
            relevant_chunks
        )

        st.text_area(
            "Best Matching Chunk",
            relevant_chunks[0],
            height=250
            )

    else:
        context = ""

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):
        st.markdown(question)

    with st.spinner("Thinking..."):
        answer = ask_gemini(
        question,
        context
        )   

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

    with st.chat_message("assistant"):
        st.markdown(answer)