import os

import discord
from dotenv import load_dotenv

from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('TOKEN')

#intents creation -- set to default for now until I figure out what they actually do
intents = discord.Intents.default()

#client creation
class base:
    client = discord.Client(intents=intents)
    guild = discord.guild.__name__
    bot = commands.Bot(command_prefix="/")


@base.client.event
async def on_ready():
    print(f'{base.client.user} has connected to Discord!')

base.client.run(TOKEN)