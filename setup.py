import os

import discord
from dotenv import load_dotenv

from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('TOKEN')

#intents creation -- set to default for now until I figure out what they actually do
intents = discord.Intents.default()

#for every instance of the bot
client = discord.Client(intents=intents)
guild = discord.guild.__name__
bot = commands.Bot(command_prefix="/")
serverDict = dict()

#Bot commands

#adds to the list of birthdays
@bot.command(name="add")
async def add(ctx, arg1:str = commands.parameter(default="Character name", description="Your character's name."), arg2:str = commands.parameter(default = "Character birthday", description = "Your character's birthday in the format <month (spelt) date (number)")):
    if arg1 in serverDict:
        print(arg1 + " is already in the list of birthdays")
    else:
        serverDict[arg1]=arg2
        print(arg1 + " (born on "+ arg2 + ") was added to the birthday list!")


#runs the bot
client.run(TOKEN)