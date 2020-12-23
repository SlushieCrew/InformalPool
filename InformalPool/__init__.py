import discord

from os import environ
from loguru import logger
from dotenv import load_dotenv
from discord.ext import commands

from .Modules._misc import misc
from .Cogs.Censys import censys_cog
from .Cogs.CrtSh import crtsh_cog
from .Cogs.Shodan import sho_cog
from .Cogs.HackerTarget import ht_cog
from .Cogs.Gulesider import yellow_cog
from .Cogs.Greetings import Greetings

# Load .env file
load_dotenv()

token = environ.get("BOT_TOKEN")
prefix = environ.get("PREFIX")
bot = commands.Bot(command_prefix=prefix)
 
# Events
@bot.event
async def on_ready():
    logger.info(f"{bot.user.name} is Ready!")

@bot.event
async def on_error(event, *args, **kwargs):
    with open('err.log', 'a') as f:
        if event == 'on_message':
            logger.error(f'Unhandled message: {args[0]}\n')
        else:
            raise

@bot.event
async def on_command_error(ctx: discord.ext.commands.Context, error):
    logger.error(error)
    if type(error) == discord.ext.commands.errors.MissingRequiredArgument:
        await ctx.send(f"Error: {error} Use ``!help {ctx.command}`` for usage")
    else:
        await ctx.send(f"Error: {error}")

# Add all the cogs 
print(misc().motd())
bot.add_cog(crtsh_cog())
bot.add_cog(censys_cog())
bot.add_cog(sho_cog())
bot.add_cog(ht_cog())
#bot.add_cog(yellow_cog())