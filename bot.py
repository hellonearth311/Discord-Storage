# imports
import os
import discord
import random

from dotenv import load_dotenv
from discord.ext import tasks

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@tasks.loop(seconds=2.0)
async def send_every_second():
    imageToSend = random.randint(1, 3)

    imgChannel = client.get_channel(1456908142615990315)
    img = discord.File(f"files/img{imageToSend}.jpg")
    
    if imgChannel:
        await imgChannel.send("testing123 hehe", file=img)

@client.event
async def on_ready():
    # main code here
    print(f'{client.user} has connected to Discord!')

    if not send_every_second.is_running():
        send_every_second.start()

client.run(TOKEN)