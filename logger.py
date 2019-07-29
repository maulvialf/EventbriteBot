from datetime import datetime

log_text_count = 0

def start():
    print("=*" * 20)
    print(datetime.now())
    print("Bot start to post\n")
    return 0

def finish():
    print("\nBot finish")
    print(datetime.now())
    print("=*" * 20)
    return 0

def printlogstat(message):
    global log_text_count
    message_text = "[*][{}].{}".format(log_text_count, message)
    print message_text
    return message_text