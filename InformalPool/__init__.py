import discord

from os import environ, listdir
from loguru import logger as log
from dotenv import load_dotenv
from discord.ext import commands

from .Modules._Utility import _Utility

from .Cogs import *

# Load .env file
load_dotenv()

TOKEN = environ.get("BOT_TOKEN")
PREFIX = environ.get("PREFIX")
BOT = commands.Bot(command_prefix=PREFIX)

# Functions that need imports but not circular imports
# TODO: move function to _Utility, with out the  with circular imports
def _list_avaliable_cogs() -> list:
    _list = listdir("./InformalPool/Cogs")
    _avaliable_cogs = [
        eval(_item.split(".py")[0]) for _item in _list if not _item.startswith("_")
    ]
    return _avaliable_cogs


# Events
@BOT.event
async def on_ready():
    log.info(f"{BOT.user.name} is Ready!")


@BOT.event
async def on_command_error(ctx: discord.ext.commands.Context, error):
    log.error(error)
    if type(error) == discord.ext.commands.errors.MissingRequiredArgument:
        await ctx.send(f"Error: {error} Use ``!help {ctx.command}`` for usage")
    else:
        await ctx.send(f"Error: {error}")


print(_Utility().motd())
for _cog in _list_avaliable_cogs():
    try:
        if _cog()._load_cog is True:
            BOT.add_cog(_cog())
            log.debug(f"Loaded {_cog().__class__.__name__}")
        else:
            log.warning(f"Not Loading {_cog().__class__.__name__}")
    except TypeError as e:
        log.error(e)