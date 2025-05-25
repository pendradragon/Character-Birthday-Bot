import discord
from discord import app_commands
from discord.ext import commands, tasks
from datetime import datetime, time 
import json
import os
import asyncio

#load_dotenv()
TOKEN = os.getenv("TOKEN")

#intents creation -- set to default for now until I figure out what they actually do
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents = intents)

#The file that is being used to save DOBs
DOB_FILE = "birthdays.json"

class BirthdayBot: 
    def __init__(self):
        self.birthdays = self.loadBirthdays()

    def loadBirthdays(self):
        #load the provided birthdays from the json file
        if os.path.exists(DOB_FILE):
                with open(DOB_FILE, 'r') as file: #opening the file with the read perms
                    return json.load(file)
        return {} #if there are no birthdays to return


    def saveBirthdays(self):
        """Saves the birthday that is provided by the user to the .json file
            Not used as a command, rather it is used as a helper command that is used in the addBirthday command"""
        with open(DOB_FILE, 'r') as file: 
            json.dump(self.birthdays, file, indent=2)

    def addBirthday(self, characterName, birth_date):
        #Adds the character's birthday to the .json file so it can be looked through for later bot implementation 
        try:
            #Validate the date format
            datetime.strftime(birth_date, '%m-%d')
            self.birthdays[characterName] = birth_date
            self.saveBirthdays()
            return True #Should it be successful, the command will return true -- should return a message saying that the date was successfully saved
        except ValueError: 
                return False

    def removeBirthday(self, characterName): 
        if characterName in self.birthdays:
            #if the character is in the birthday storage
            del self.birthdays[characterName] 
            self.saveBirthdays() #saving the deleting of the character's date
            return True #later used for a message that is presented to the user
        return False 

    def getTodaysBirthdays(self): 
        """Used to go through the .json file for the current day's date
            Not used as a command
            Used as a helper command that will be used in the loop that will be run daily"""

        #Getting the current date in the correct format so it can be compared against the dates in the .json file
        today = datetime.now.strftime('%m-%d')
        todaysBirthdays = []

        #actual checking loop
        for character, birthday in self.birthdays.item():
            if birthday == today: 
                todaysBirthdays.append(character) #appends the particular character's name 

        return todaysBirthdays

#initalize the birthday manager 
birthdayManager = BirthdayBot()

#starting the bot
bot.run(TOKEN)
