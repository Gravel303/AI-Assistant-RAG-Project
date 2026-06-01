import streamlit as st
import os

from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

st.title("AI Study Assistant")

question = st.text_input(
    "Ask a question:"
)

if st.button("Generate Answer"):

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=question
    )

    st.write(response.text)