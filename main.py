import os

import discord
from dotenv import load_dotenv

from discord.ext import commands

#commands code imports
from dictCommands import dictBasics

load_dotenv()
TOKEN = os.getenv('TOKEN')

#intents creation -- set to default for now until I figure out what they actually do
intents = discord.Intents.default()

#used universally throughout the bot
class base:
    client = discord.Client(intents=intents)
    guild = discord.guild.__name__
    bot = commands.Bot(command_prefix="c!")
    serverDict = dict()

    bDayMessage = str()

#basic setup commands
@base.bot.command(name="setMessage")
async def setMessage(ctx, arg1:str = commands.parameter(default = "The message that is sent every time it is a character's birthday.", description = None)):
    base.bDayMessage = arg1

@base.bot.command(name = "help")
async def help(ctx):
    print("# Character Birthday Bot Help #" + "\n" +
          "setMessage -- sets the message that is sent every time it is a character's birthday" + "\n"+
          "add -- adds a character to the bot's birthday logs" + "\n" +
          "remove -- removes a character from the bot's birthday logs" + "\n" +
          "findDOB -- finds the character with the entered date of birth")
    
#bot commands from the dictCommands file
@base.bot.command(name = "add")
async def add(ctx, arg1:str = commands.parameter(default="Character name", description="Insert your characters name"), arg2:str = commands.parameter(default = "Your character's date of birth", description = "Insert your character's date of birth in the format <month (spelt) date (number)")):
    dictBasics.add(arg1, arg2)

@base.bot.command(name = "remove")
async def remove(ctx, arg1:str = commands.parameter(default= "Character name", description="The name of the character you want to remove from the birthday logs")):
    dictBasics.remove(arg1)

@base.bot.command(name="findDOB")
async def findDOB(ctx, arg1:str = commands.parameter(default = "Character name", description="Finds the date of the birth of the provided character")):
    dictBasics.findDOB(arg1)


#runs the bot
base.client.run(TOKEN)