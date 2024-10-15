import os
from datetime import datetime

#discord imports
import discord
from discord.ext import commands, tasks

#Security is wild
from dotenv import load_dotenv

#Custom commands importing
from dictCommands import add_character, remove_character, getDOB, get_character_by_DOB
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

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    birthday_check.start() #starts the checking loop

#Command to add characters to the dictionary
@bot.command()
async def add(ctx, name: str, date: str):
    #DOBS should be in the format should be in the format MM-DD
    try:
        datetime.strptime(date, '%m-%d')
        add_character(name, date)
        await ctx.send(f"Added {name} with their birthday on {date}.")

    except ValueError:
        await ctx.send(f"Invalid date format. Please use MM-DD.")
        
#Command to remove a character from the dictionary
@bot.command()
async def remove(ctx, name: str):
    if name in birthdays:
        remove_character(name)
        await ctx.send(f"Removed {name} from the list.")

    else:
        await ctx.send(f"{name} is not in the list.")

#Command to find DOB by character name
@bot.command()
async def findDOB(ctx, name:str):
    dob = getDOB(name)
    if dob: #if the dob is in the list
        await ctx.send(f"{name}'s birthday is not on {dob}.")
    else: #if not in the list
        await ctx.send(f"No birthday found for {name} found in the list.")

#Command to find characters by their DOB
@bot.command()
async def findByDOB(ctx, date: str):
    try: #tries all characters with the specified DOB -- run if in the format MM-DD
        datetime.strptime(date, '%m-%d')
        characters = get_character_by_DOB(date)

        if characters: #if there are character(s) found in the list with the desired DOB
            await ctx.send(f"The following characters have a birthday on {date}: {','.join(characters)}.")

        else: #if there are no characters with the specified DOB
            await ctx.send(f"No characters in the list were found with a birthday on {date}.")
        
    except ValueError: #if the date is not in the correct format
        await ctx.send("Invalid date format. Please use MM-DD.")

#command to send a custom birthday message template
@bot.command()
async def setMessage(ctx, *, template: str):
    #defaults
    if template.lower() == "default":
        default_message = "🎉 Today is {name}'s birthday! 🎉"
        setMessage(default_message)

    #custom message
    elif "{name}" in template:
        setMessage(template)
        await ctx.send("Custom birthday message as been set.")  
    
    #incorrect format
    else:
        await ctx.send("Invalid template. \n\t Hint: make sure to include '{name}' for where the character's name will be in the template.")

#Command to set the preferred channel
@bot.command()
async def setChannel(ctx):
    #sets the CURRENT channel as the preferred channel for birthday messages
    setChannel(ctx.channel.id)
    await ctx.send(f"Birthday messages will now be sent to {ctx.channel.mention}.")

