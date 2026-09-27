print("=== My Python Chatbot ===")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Bot: Goodbye!")
        break

    elif user_input.lower() == "hi":
        print("Bot: Hello sir!")

    elif user_input.lower() == "hello":
        print("Bot: Hello sir!")

    elif user_input.lower() == "how are you":
        print("Bot: I'm doing great! How can I help you?")

    elif user_input.lower() == "who are you":
        print("Bot: I'm your Python bot.")

    elif user_input.lower() == "what is python":
        print("Bot: Python is a fundamental programming language.")

    else:
        print("Bot: Unknown input.\nSorry sir, I don't understand that yet.")