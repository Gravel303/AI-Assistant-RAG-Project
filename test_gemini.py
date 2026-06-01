import os
from dotenv import load_dotenv
from google import genai

# Load .env
load_dotenv()

# Create client
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

# Generate response
response = client.models.generate_content(
    model="gemini-2.5-flash",
   contents="""
You are a networking professor.

Explain TCP congestion control to a BTech student.
"""
)

print(response.text)