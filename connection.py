import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')

#intents creation -- set to default for now until I figure out what they actually do
intents = discord.Intents.default()

#client creation
client = discord.Client(intents=intents)
guild = discord.guild.__name__

#will be referenced in the commands portion of the program
serverDict = dict()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

client.run(TOKEN)