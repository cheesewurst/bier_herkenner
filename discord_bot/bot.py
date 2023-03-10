import os
from dotenv import load_dotenv
import config
import discord
import asyncio

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print("Online and ready for service!")

async def setup():
    print("Setting up....")

async def main():
    await setup()
    await client.start(TOKEN)

asyncio.run(main())
