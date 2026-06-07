import streamlit as st

import os 

from utils.storage_manager import (load_chunks, load_index, save_chunks, save_index)

from utils.fast_semantic_retriever import fast_semantic_retrieve
# from utils.retriever import retrieve_chunks

from utils.text_chunker import chunk_text

from utils.gemini_client import ask_gemini

from utils.pdf_processor import extract_text_from_pdf

from utils.embeddings import get_embedding

from utils.faiss_manager import build_faiss_index

from utils.faiss_retriever import faiss_retrieve

from utils.query_rewriter import (
    rewrite_query
)

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

# if "chunk_embeddings" not in st.session_state:
#     st.session_state.chunk_embeddings = []

if "faiss_index" not in st.session_state:
    st.session_state.faiss_index = None

if "retrieved_chunks" not in st.session_state:
    st.session_state.retrieved_chunks = []


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
    if not st.session_state.chunks:
        pdf_text = extract_text_from_pdf(
            uploaded_file
        )

        chunks = chunk_text(pdf_text)

        chunk_embeddings = []

        with st.spinner(
            "Generating embeddings..."
        ):

            # for chunk in chunks:

            #     embedding = get_embedding(
            #         chunk
            #     )

            #     chunk_embeddings.append(
            #         embedding
            #     )
            for i, chunk in enumerate(chunks):

                try:

                    embedding = get_embedding(
                        chunk
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

        # st.session_state.chunk_embeddings = (
        #     chunk_embeddings
        # )

        index = build_faiss_index(
            chunk_embeddings
            )
        
        save_chunks(chunks)

        save_index(index)

        st.session_state.faiss_index = index

        st.session_state.current_pdf = (
            uploaded_file.name
        )

        st.success("PDF loaded!")

        st.text_area(
        "PDF Preview",
        pdf_text[:3000],
        height=300
        )  

st.sidebar.write(
    f"Loaded Chunks: {len(st.session_state.chunks)}"
)

if st.session_state.faiss_index:
    st.sidebar.write(
        f"Index Size: "
        f"{st.session_state.faiss_index.ntotal}"
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
            relevant_chunks
        )

        st.text_area(
            "Best Matching Chunk",
            relevant_chunks[0],
            height=250
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
                    f"### Source {i}"
                )

                st.write(
                    chunk[:1000]
                )   