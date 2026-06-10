from utils.gemini_client import client

def generate_quiz(
    text
):
    prompt = f"""
    You are a study assistant.

    Create a quiz from the document.

    Generate:

    - 10 multiple choice questions
    - 4 options for each question
    - Mark the correct answer

    Format clearly.

    Document:

    {text[:20000]}
    """
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text