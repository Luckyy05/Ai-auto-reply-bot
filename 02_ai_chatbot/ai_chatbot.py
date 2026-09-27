from gemini_api import get_ai_response
from reply_logic import should_reply
print("=== AI CHATBOT ===")
while True:
    user_input = input("you: ").lower().strip()
    if user_input == "exit":
        print("bot: Goodbye!")
        break 
    if should_reply(user_input):
         response = get_ai_response(user_input)
         print("bot:",response)