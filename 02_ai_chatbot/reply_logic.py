MAX_MESSAGE_LEN = 1000
IGNORED_MESSAGE =["good morning",
    "good night",
    "ok",
    "okay"
]
def should_reply(message):
    message = message.strip().lower()
    if not message:# if there is no  message  do nopt rply 
        return False
    
    if len(message) > MAX_MESSAGE_LEN:
        return False
    if message  in IGNORED_MESSAGE:
        return False 
    return True 
