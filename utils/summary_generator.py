from utils.gemini_client import client

def generate_summary(
    text
):  
    prompt = f"""
You are a study assistant.

Create a study summary of the document.

Format your response as:

# Main Topics

# Important Concepts

# Key Points

# Exam Revision Notes

Document:

{text[:20000]}
"""
    response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt
    )

    return response.text