# from bot.gemini_api import get_ai_response
# from bot.reply_logic import should_reply

# def main():
#     print("=== AI AUTO-REPLY BOT ===")

   

#     # Check whether bot should reply
#     if not should_reply(sender, message, "Lucky"):
#         print("Bot: Message ignored.")
#         return

#     # Generate AI response
#     response = get_ai_response(message)

#     print("Bot:", response)

#     # Send AI response to WhatsApp
#     send_message(response)


# if __name__ == "__main__":
#     main()
from bot.whatsapp import WhatsApp
from bot.groq_api import get_ai_response
from bot.reply_logic import should_reply


def main():

    print("=== AI AUTO-REPLY BOT ===")

    whatsapp = WhatsApp()

    try:

        # Start WhatsApp
        whatsapp.start()

        # User manually selects the chat
        input(
            "Open the chat you want to monitor, "
            "then press ENTER..."
        )

        # Get latest message
        latest = whatsapp.get_latest_message()

        if not latest:
            print("No message found.")
            return

        sender = latest["sender"]
        message = latest["text"]

        print("\n--- MESSAGE ---")
        print("Sender:", sender)
        print("Message:", message)

        # Check whether bot should reply
        if not should_reply(sender, message, "Lucky"):

            print("Bot: Message ignored.")
            return

        # Generate AI response
        response = get_ai_response(message)

        print("Bot:", response)

        # Send response to WhatsApp
        whatsapp.send_message(response)

        print("Message sent successfully.")

        input("Press ENTER to close WhatsApp...")

    finally:

        whatsapp.close()


if __name__ == "__main__":
    main() 