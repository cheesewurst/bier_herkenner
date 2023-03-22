import discord
from discord import app_commands
from discord.ext import commands

class StockChecker(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready():
        print('Stock checker cog ready!')

    @app_commands.command(name='stock', description='Sends amount of beer left in the "Keet Tumke" keet')
    async def stock(interaction: discord.Interaction):
        await interaction.response.send_message("No stock loaded :(")

    

async def setup(bot) -> None:
    await bot.add_cog(StockChecker(bot))