from google import genai
import os
from dotenv import load_dotenv
import numpy as np

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

def get_embedding(text):
    
    result = client.models.embed_content(
        model="gemini-embedding-001",
        contents=text
    )

    return result.embeddings[0].values

def cosine_similarity(vec1, vec2):

    vec1 = np.array(vec1)
    vec2 = np.array(vec2)

    return np.dot(vec1, vec2) / (
        np.linalg.norm(vec1)
        * np.linalg.norm(vec2)
    )

# def cosine_similarity(vec1, vec2):

#     vec1 = np.array(vec1)
#     vec2 = np.array(vec2)

#     return np.dot(vec1, vec2) / (
#         np.linalg.norm(vec1)
#         * np.linalg.norm(vec2)
#     )

