MAX_MESSAGE_LEN = 1000
def should_reply(message):
    message = message.strip()
    if not message:# if there is no  message  do nopt rply 
        return False
    
    if len(message) > MAX_MESSAGE_LEN:
        return False
        
    return True 
