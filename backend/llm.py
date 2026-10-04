import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
MODEL = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")


def ask_llm(prompt: str) -> str:
    response = client.models.generate_content(model=MODEL, contents=prompt)
    return response.text