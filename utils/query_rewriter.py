from utils.gemini_client import client

def rewrite_query(
    question,
    chat_history
):
    prompt = f"""
You are a query rewriting assistant.

Your task is to rewrite the user's
question so that it is fully
self-contained.

Use the conversation history
to resolve references such as:

- it
- they
- this
- that
- the protocol
- the system

Return ONLY the rewritten question.

Conversation History:

{chat_history}

Question:

{question}
"""
    response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt
)

    return response.text.strip()