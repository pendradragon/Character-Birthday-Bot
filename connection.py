import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('MTI1NTYwODk3NzY1NjY0NzcxMA.GUi3S1.xfC4C2sd3znhvCKK8KaFF4B4TbH3q6SAxPXxYw')

#client creation
client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

client.run(TOKEN)