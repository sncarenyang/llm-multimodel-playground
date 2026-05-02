import os
from google import genai
from config import GEMINI_MODEL

def ask_gemini(prompt):
    client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))
    response = client.models.generate_content(
        model=GEMINI_MODEL,
        contents=prompt
    )
    return response.text
