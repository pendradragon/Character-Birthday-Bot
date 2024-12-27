import os
from datetime import datetime

#discord imports
import discord
from discord import app_commands
from discord.ext import commands, tasks

#Security is wild
import os

#Custom commands importing
from dictCommands import add_character, remove_character, getDOB, get_character_by_DOB
#from checker import check_birthdays

#importing data be like
from birthdayData import birthdays, setMessage, getMessage
from configs import setChannel, getChannel

#load_dotenv()
TOKEN = os.getenv("TOKEN")

#intents creation -- set to default for now until I figure out what they actually do
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents = intents)

#defining the bot's command tree for slash command adaptation
class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #help command creation
    @app_commands.command(name = "help", description = "Lists available commands and description.")
    async def help_command(self, interaction: discord.Interaciton): #I am so HTML brained I'm going to format it like that
            embed = discord.Embed(
                title = "Help Menu"
                description = "Available commands"
                color = discord.Color.blue()
        )
        
            embed.add_field(
                name = "/help"
                value = "Displays this menu."
                inline = False
        )
            embed.add_field(
                name = "/add <character name> <date of birth (MM-DD)>"
                value = "Add a character to the birthday list."
                inline = False
        )
            embed.add_field(
                name = "/remove <character name>"
                value = "Remove a character from the list."
                inline = False
        )
            embed.add_field(
                name = "/findDOB <character name>"
                value = "Find the date of birth of a particular character."
                inline = False
        )    
            embed.add_field(
                name = "/findByDOB <date of birth>"
                value = "Find the character with the specific birthday."
                inline = False
        )

        await interaction.response.send_message(embed=embed)

#register the juicy cog
async def setup(bot):
        await bot.add_cog(Help(bot))

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    birthday_check.start() #starts the checking loop
    await bot.tree.sync() #register commands when the bot is ready

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

@tasks.loop(hours=24) #run once per day
async def birthday_check():
    today = datetime.now().strftime("%m-%d")
    messageChannel_ID = getChannel()
    messageChannel = bot.get_channel(messageChannel_ID)

    if messageChannel is None:
            await ctx.send(f'Channel ID {messageChannel_ID} is not found. Please set the channel you want to use with "!setChannel".')
            return 

    #time for the actual loop
    names = [name for name, bday in birthdays.items(), if bday == today]

    if names: #if there are names that need to be printed
        for name in names:
            custom_message = getMessage()
            await ctx.send(custom_message.format(name=name))

    else:
        #for debugging purposes so ik if there is something wrong with it not runnning every 24 hours
        await ctx.send(f"There are no birthdays today, {today}.")
    

#starting the bot
bot.run(TOKEN)
