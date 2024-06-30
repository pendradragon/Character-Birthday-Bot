import discord
from discord.ext import commands

from setup import base
from serverSetup import serverStuff

class commands:
    #add command
    @base.bot.command(name='add')
    async def add(ctx, arg1:str = commands.parameter(defualt = 'Character name', description = "Your character's name goes here"), arg2:str = commands.parameter(default = "Birthday", description = "Insert the date of birth in the format <month (spelt) day (number)>")):
        for entry in serverStuff.serverDict:
            #runs if the character is ALREADY in the dictionary
            if entry.key == arg1:
                print(arg1 + " is already in the birthday logs!")
            
            #runs if the character is NOT in the dictionary
            else:
                serverStuff.serverDict[arg1]=arg2