import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')

#intents creation -- set to default for now until I figure out what they actually do
intents = discord.Intents.default()
intents.members = True

#client creation
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

client.run(TOKEN)