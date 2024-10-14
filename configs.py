#Have it so that the user can chose where to send the birthday message

preferred_channel_id = None #starts out as None, can be changed via commands

def setChannel(channel_id):
    global preferred_channel_id
    preferred_channel_id = channel_id

def getChannel():
    return preferred_channel_id