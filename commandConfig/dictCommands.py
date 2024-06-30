import discord
from discord.ext import commands

from setup import base
from serverSetup import serverStuff

class commands:
    #add command
    @base.bot.command(name='add')
    async def add(ctx, arg1:str = commands.parameter(defualt = 'Character name', description = "Your character's name goes here"), arg2:str = commands.parameter(default = "Birthday", description = "Insert the date of birth in the format <month (spelt) day (number)>")):
        #runs if the character is in the dictionary alread
        if arg1 in serverStuff.serverDict:
            print(arg1 + " is already in the birth logs!")
        
        #runs if the character is not in the dictionary -- should add it
        else:
            serverStuff.serverDict[arg1] = arg2