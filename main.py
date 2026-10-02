from bot.gemini_api import get_ai_response
from bot.reply_logic import should_reply

def main():
    print("=== AI AUTO-REPLY BOT ===")

   

    # Check whether bot should reply
    if not should_reply(sender, message, "Lucky"):
        print("Bot: Message ignored.")
        return

    # Generate AI response
    response = get_ai_response(message)

    print("Bot:", response)

    # Send AI response to WhatsApp
    send_message(response)


if __name__ == "__main__":
    main()