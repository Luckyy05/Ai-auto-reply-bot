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

        print("\n--- INITIAL MESSAGE ---")
        print("Sender:", latest["sender"])
        print("Message:", latest["text"])

        last_message = latest

        while True:

            print("\nWaiting for a new message...")

            new_message = whatsapp.wait_for_new_message(last_message)

            print("\n--- NEW MESSAGE ---")
            print("Sender:", new_message["sender"])
            print("Message:", new_message["text"])
            print("Metadata:", new_message["metadata"])

            # Update last seen message
            last_message = new_message

            # Check whether bot should reply
            if not should_reply(
                new_message["sender"],
                new_message["text"],
                "Lucky"
            ):
                print("Bot: Message ignored.")
                continue

            # Generate AI response
            response = get_ai_response(
                new_message["text"]
            )

            print("Bot:", response)

            # Send response
            whatsapp.send_message(response)

            print("Message sent successfully.")

    finally:

        whatsapp.close()


if __name__ == "__main__":
    main() 