from gemini_api import get_ai_response
print("=== AI CHATBOT ===")
while True:
    user_input = input("you: ").lower().strip()
    if user_input.lower() == "exit":
        print("bot: Goodbye!")
        break 
    response = get_ai_response(user_input)
    print("bot:",response)