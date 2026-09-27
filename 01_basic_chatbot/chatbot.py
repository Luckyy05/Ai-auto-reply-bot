print("=== My Python Chatbot ===")

while True:
    user_input = input("You: ").lower().strip()

    if user_input == "exit":
        print("Bot: Goodbye!")
        break

    elif user_input == "hi":
        print("Bot: Hello sir!")

    elif user_input == "hello":
        print("Bot: Hello sir!")

    elif user_input == "how are you":
        print("Bot: I'm doing great! How can I help you?")

    elif user_input == "who are you":
        print("Bot: I'm your Python bot.")

    elif user_input == "what is python":
        print("Bot: Python is a fundamental programming language.")

    else:
        print("Bot: Unknown input.\nSorry sir, I don't understand that yet.")