from pypdf import PdfReader
import streamlit as st


@st.cache_data
def extract_text_from_pdf(pdf_file):
   
    reader = PdfReader(pdf_file)

    text = ""

    for page_num, page in enumerate(reader.pages):

        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text

