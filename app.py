import streamlit as st

from utils.gemini_client import ask_gemini

st.set_page_config(
    page_title="AI Study Assistant",
    page_icon="📚"
)

st.title("📚 AI Study Assistant")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])


question = st.chat_input(
    "Ask a study question..."
)

if question:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):
        st.markdown(question)

    with st.spinner("Thinking..."):
        answer = ask_gemini(question)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

    with st.chat_message("assistant"):
        st.markdown(answer)