from datetime import datetime

from birthdayData import birthdays
from birthdayData import message_template

from configs import getChannel

async def check_birthdays(bot):
    # checks if today's date matches any birthday in the directory
    today = datetime.now().strftime('%m-%d')
    sendChannel = getChannel()

    if sendChannel: #if there is a channel ID saved there
        channel = bot.get_channel(sendChannel)

        if channel:
            for name, date in birthdays.items():
                if date == today:
                    #format the message using the template that the user picked out
                    sentMessage = message_template.format(name=name)
                    await channel.send(sentMessage)