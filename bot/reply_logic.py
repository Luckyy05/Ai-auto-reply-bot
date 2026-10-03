MAX_MESSAGE_LENGTH = 1000

IGNORED_MESSAGES = [
    "good morning",
    "good night",
    "ok",
    "okay"
]


def should_reply(sender, message, my_name): 
    sender = sender.strip().lower()
    message = message.strip().lower() 
    my_name = my_name.strip().lower()
    
    # Don't reply to my own messages
    if sender == my_name:
        return False

    # Don't reply to empty messages
    if not message:
        return False

    # Don't process extremely long messages
    if len(message) > MAX_MESSAGE_LENGTH:
        print("message is too long")
        return False

    # Ignore predefined messages
    if message in IGNORED_MESSAGES:
        print("message ignored" )
        return False

    return True