import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

def ask_gemini(question):

    prompt = f"""
    You are a helpful study assistant.

    Explain concepts clearly and simply.

    Question:
    {question}
    """

    try:

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:

        return (
    "Sorry, something went wrong while "
    f"contacting Gemini.\n\n{str(e)}"
)
