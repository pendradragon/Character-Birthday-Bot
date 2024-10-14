#Global variables that are used throughout the code

birthdays = {}
message_template = "🎉 Today is {name}'s birthday! 🎉"

def setMessage(template):
    # sets the custom message as the message to be sent
    global message_template
    message_template = template

def getMessage():
    return message_template