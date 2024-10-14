from datetime import datetime

from birthdayData import birthdays
from birthdayData import message

from configs import getChannel

async def check_birthdays(bot):
    # checks if today's date matches any birthday in the directory
    today = datetime.now().strftime('%m-%d')
    