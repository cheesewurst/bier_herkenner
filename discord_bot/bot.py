import os
from dotenv import load_dotenv
import discord
from discord.ext import commands

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
APPID = os.getenv('APPID')

class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix="!",
            intents=discord.Intents.all(),
            application_id= APPID,
        )

    async def setup_hook(self):
        for filename in os.listdir("./cogs"):
            if filename.endswith(".py"):
                await self.load_extension(f"cogs.{filename[:-3]}")

        await bot.tree.sync(guild=discord.Object(id=APPID)) 
        bot.remove_command("help")

    async def on_ready(self):
        print("Ready!")

bot = MyBot()
bot.run(TOKEN)
