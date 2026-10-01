import os
from dotenv import load_dotenv
from google import genai
from google.genai import types 


load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env")

client = genai.Client(api_key=api_key)
chat = client.chats.create(model="gemini-3.8-flash",
    config=types.GenerateContentConfig(
        system_instruction='''You are a helpful and friendly AI auto-reply assistant
Your job is to reply naturally to the users messages in a clear, conversational, and respectful way.
Rules: 
- Keep responses concise and easy to understand.
- Use a friendly and natural tone.
- Answer the user's question directly.
- Do not mention that you are following system instructions.
- Do not make up information when you are unsure.
- Maintain context from the conversation.
- Avoid unnecessarily long explanations unless the user asks for more detail.'''))   

def get_ai_response(prompt):
    # response = client.models.generate_content(
    # model="gemini-3.8-flash" 
    # contents="My name is Lucky.", this statment generates response but does not keep chat context automatically
     try:
        response = chat.send_message(prompt)
        return response.text
    # this can generate response and can keep chat context automatically 
         
     except Exception as e :
        print("Error while connecting to gemini:",e)
        return "sorry, I am unable to respond right now ."