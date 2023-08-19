import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
 await bot.load_extension(name="cogs.dispatch", package=None)


load_dotenv()
bot.run(os.getenv("TOKEN"))
