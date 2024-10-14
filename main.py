import os
from datetime import datetime

#discord imports
import discord
from discord.ext import commands, tasks

#Security is wild
from dotenv import load_dotenv

#Custom commands importing
from dictCommands import add, remove, getDOB, get_character_by_DOB
from checker import check_birthdays

#importing data be like
from birthdayData import birthdays, setMessage, getMessage
from configs import setChannel, getChannel

load_dotenv()
TOKEN = os.getenv('TOKEN')

#intents creation -- set to default for now until I figure out what they actually do
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents = intents)