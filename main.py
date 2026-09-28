from ai_chatbot.gemini_api import get_ai_response
from ai_chatbot.reply_logic import should_reply

def main():
    print("=== AI CHATBOT ===")

    my_name = "Lucky".strip().lower()
    while True:

        sender = input("Sender:")
        message = input("message:")

        if message.lower().strip() == "exit":
            print("bot: Goodbye!")
            break 

        if should_reply(sender, message,my_name):
            response = get_ai_response(message)
            print("bot:",response)

        else :
            print("bot: message is ignored")

if __name__ == "__main__":
    main()