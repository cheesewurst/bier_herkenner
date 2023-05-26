import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
from api import get_stock

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
APPID = os.getenv('APPID')
intents = discord.Intents.default()

bot = commands.Bot(command_prefix= '.', intents = intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')

@bot.slash_command()
async def stock(ctx: commands.Context):
    await ctx.send(f'Current stock is, {get_stock()}!')

bot.run(TOKEN)
