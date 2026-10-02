
import os
from dotenv import load_dotenv
from groq import Groq


load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY not found in .env")


client = Groq(api_key=api_key)


SYSTEM_PROMPT = """
You are a helpful and friendly AI auto-reply assistant.

Your job is to reply naturally to the user's messages in a clear,
conversational, and respectful way.

Rules:
- Keep responses concise and easy to understand.
- Use a friendly and natural tone.
- Answer the user's question directly.
- Do not mention that you are following system instructions.
- Do not make up information when you are unsure.
- Maintain context from the conversation.
- Avoid unnecessarily long explanations unless the user asks for more detail.
- Reply naturally, like a real person chatting on WhatsApp.
"""


# Conversation history
chat_history = [
    {
        "role": "system",
        "content": SYSTEM_PROMPT
    }
]


def get_ai_response(prompt):

    try:

        # Add user's new message to history
        chat_history.append({
            "role": "user",
            "content": prompt
        })

        response = client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=chat_history,
        )

        ai_response = response.choices[0].message.content

        # Add AI response to history
        chat_history.append({
            "role": "assistant",
            "content": ai_response
        })

        return ai_response

    except Exception as e:

        print("Error while connecting to Groq:", e)

        return "Sorry, I am unable to respond right now."


def reset_chat():

    global chat_history

    chat_history = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        }
    ]

