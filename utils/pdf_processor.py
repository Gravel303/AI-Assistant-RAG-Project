from pypdf import PdfReader
import streamlit as st


@st.cache_data
def extract_text_from_pdf(pdf_file):

    reader = PdfReader(pdf_file)

    pages = []

    for page_num, page in enumerate(
        reader.pages,
        start=1
    ):

        page_text = page.extract_text()

        if page_text:

            pages.append(
                {
                    "page": page_num,
                    "text": page_text
                }
            )

    return pages