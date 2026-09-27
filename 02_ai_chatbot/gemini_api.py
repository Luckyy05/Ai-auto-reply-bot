import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env")

client = genai.Client(api_key=api_key)
chat = client.chats.create( model="gemini-3.8-flash")
def get_ai_response(prompt):
    response = chat.send_message(prompt)
    return response.text