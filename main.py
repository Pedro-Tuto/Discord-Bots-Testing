import discord
from discord.ext import commands
from music import Player

TOKEN = '####################################################'

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user.name} está pronto")

bot.add_cog(Player(bot))
bot.run(TOKEN)