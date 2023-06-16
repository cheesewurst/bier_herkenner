import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
from api import get_stock
import requests

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
APPID = os.getenv('APPID')
intents = discord.Intents.default()
url = 'http:127.0.0.1:8000/get_stock'
bot = commands.Bot(command_prefix= '.', intents = intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')

@bot.slash_command()
async def stock(ctx: commands.Context):
    response = requests.get(url)
    stock = ''

    if response.status_code == 200:
        data = response.json()
        stock = data['stock']
    else :
        stock = "no stock found"
    await ctx.send(f'Current stock is, {stock}!')

bot.run(TOKEN)
