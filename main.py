from bot.gemini_api import get_ai_response
from bot.reply_logic import should_reply
from bot.whatsapp import activate_whatsapp, send_message , click_search_box, search_chat


def main():
    print("=== AI AUTO-REPLY BOT ===")

    # Temporary manual input
    sender = input("Sender: ")
    message = input("Message: ")

    # Activate WhatsApp Desktop
    activate_whatsapp()
    search_chat("Lucky")

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