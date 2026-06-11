from utils.gemini_client import client
def generate_flashcards(
    text
):
    prompt = f"""
    You are a study assistant.

    Create 15 study flashcards
    from the document.

    Format:

    Q: Question

    A: Answer

    Requirements:

    - Cover important concepts
    - Keep answers concise
    - Focus on exam preparation
    - Avoid duplicate flashcards
    - Each flashcard should test a different concept

    Document:

    {text[:20000]}
    """
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text