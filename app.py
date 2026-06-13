import streamlit as st

import os 

from utils.storage_manager import (load_chunks, load_index, save_chunks, save_index)

from utils.text_chunker import chunk_text

from utils.gemini_client import ask_gemini

from utils.pdf_processor import extract_text_from_pdf

from utils.embeddings import get_embedding

from utils.faiss_manager import build_faiss_index

from utils.faiss_retriever import faiss_retrieve

from utils.query_rewriter import (
    rewrite_query
)

from utils.summary_generator import (
    generate_summary
)

from utils.quiz_generator import (
    generate_quiz
)

from utils.flashcard_generator import generate_flashcards

st.set_page_config(
    page_title="AI Study Assistant",
    page_icon="📚"
)

st.title("📚 AI Study Assistant")
st.caption(
    "Upload a PDF and study using AI chat, summaries, quizzes, and flashcards."
)

if "current_pdf" not in st.session_state:
    st.session_state.current_pdf = None
with st.sidebar:
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

if "faiss_index" not in st.session_state:
    st.session_state.faiss_index = None

if "retrieved_chunks" not in st.session_state:
    st.session_state.retrieved_chunks = []

if "summary" not in st.session_state:
    st.session_state.summary = ""

if "quiz" not in st.session_state:
    st.session_state.quiz = ""

if "flashcards" not in st.session_state:
    st.session_state.flashcards = ""

if (
    os.path.exists("data/chunks.pkl")
    and
    os.path.exists("data/faiss.index")
    and
    not st.session_state.chunks
):

    st.session_state.chunks = (
        load_chunks()
    )

    st.session_state.faiss_index = (
        load_index()
    )

if (
    uploaded_file
    and uploaded_file.name
    != st.session_state.current_pdf
):
        pages = extract_text_from_pdf(
            uploaded_file
        )

        chunks = chunk_text(pages)
        st.session_state.current_pdf = (
                uploaded_file.name
            )
            
        chunk_embeddings = []

        with st.spinner(
                "Generating embeddings..."
            ):
                for i, chunk in enumerate(chunks):

                    try:

                        embedding = get_embedding(
                            chunk["text"]
                        )

                        chunk_embeddings.append(
                        embedding
                        )

                    except Exception as e:

                        st.error(
                            f"Failed at chunk "
                            f"{i + 1}: {e}"
                        )

                        break
        st.write(
            f"Stored {len(chunk_embeddings)} embeddings"
        )

        st.session_state.chunks = chunks

        index = build_faiss_index(
                chunk_embeddings
                )
            
        save_chunks(chunks)

        save_index(index)

        st.session_state.faiss_index = index

        st.session_state.summary = ""

        st.session_state.summary = ""

        st.session_state.flashcards = ""

        st.success("PDF loaded!")

if uploaded_file:
    st.sidebar.success(
        f"Loaded PDF:\n{st.session_state.current_pdf}"
    )

with st.sidebar:

    if st.button(
        "📄 Generate Summary"
    ): 
        if st.session_state.chunks and uploaded_file:
            document_text = "\n\n".join(
            chunk["text"]
            for chunk in st.session_state.chunks
            )
            with st.spinner(
            "Generating summary..."
            ):

                st.session_state.summary = (
                    generate_summary(
                        document_text
                    )
                )
        else:
            st.warning(
                "Please upload a PDF first."
            )

    if st.button(
        "📝 Generate Quiz"
    ):
        if st.session_state.chunks and uploaded_file:
            document_text = "\n\n".join(
                chunk["text"]
                for chunk in st.session_state.chunks
            )

            with st.spinner(
                "Generating quiz..."
            ):

                st.session_state.quiz = (
                    generate_quiz(
                        document_text
                    )
                )


    if st.button(
        "🃏 Generate Flashcards"
    ):
        if st.session_state.chunks and uploaded_file:
            document_text = "\n\n".join(
                chunk["text"]
                for chunk in st.session_state.chunks
            )

            with st.spinner(
                "Generating flashcards..."
            ):

                st.session_state.flashcards = (
                    generate_flashcards(
                        document_text
                    )
                )


if st.session_state.summary:

    with st.expander(
        "📄 Document Summary"
    ):

        st.markdown(
            st.session_state.summary
        )

if st.session_state.quiz:

    with st.expander(
        "📝 Document Quiz"
    ):
        st.text_area(
        "Document Quiz",
        st.session_state.quiz,
        height=600
        )

if st.session_state.flashcards:

    with st.expander(
        "🃏 Document Flashcards"
    ):

        st.text_area(
            "Document Flashcards",
            st.session_state.flashcards,
            height=600
        )

if question:

    if uploaded_file:

        chat_history = ""
        for message in st.session_state.messages:

            chat_history += (
                f"{message['role']}: "
                f"{message['content']}\n"
            )

        rewritten_question = rewrite_query(
            question,
            chat_history
        )

        st.sidebar.write(
        "Rewritten Query:"
        )

        st.sidebar.write(
        rewritten_question
        )

        relevant_chunks = (
            faiss_retrieve(
                rewritten_question,
                st.session_state.faiss_index,
                st.session_state.chunks
            )
        )

        st.session_state.retrieved_chunks = (
                relevant_chunks
        )

        context = "\n\n".join(
            chunk["text"]
            for chunk in relevant_chunks
        )

    else:
        context = ""
    
        chat_history = ""
    
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
        context,
        chat_history
        )   

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

    with st.chat_message("assistant"):
        st.markdown(answer)

    if st.session_state.retrieved_chunks:

        with st.expander(
            "View Retrieved Sources"
        ):

            for i, chunk in enumerate(
                st.session_state.retrieved_chunks,
                start=1
            ):

                st.markdown(
                    f"### Source {i} "
                    f"(Page {chunk['page']})"
                )

                st.write(
                    chunk["text"][:1000]
                )   