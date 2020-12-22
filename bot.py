#!/usr/bin/env python3
import discord
import random

from os import environ
from loguru import logger
from dotenv import load_dotenv
from discord.ext import commands

from InformalPool.censys import censys_cog
from InformalPool.hacker_target import ht_cog
from InformalPool.shodan import sho_cog
from InformalPool.crt_sh import crtsh_cog
from InformalPool.yellowpages_no import yellow_cog

load_dotenv()

token = environ.get("BOT_TOKEN")
prefix = environ.get("PREFIX")
client = discord.Client()
bot = commands.Bot(command_prefix=prefix)


def motd():
    """ Gotta need a fancy motd """
    print(
        ".___        _____                           .__ __________             .__   \n"
        "|   | _____/ ____\___________  _____ _____  |  |\______   \____   ____ |  |  \n"
        "|   |/    \   __\/  _ \_  __ \/     \\__   \ |  | |     ___/  _ \ /  _ \|  |  \n"
        "|   |   |  \  | (  <_> )  | \/  Y Y  \/ __ \|  |_|    |  (  <_> |  <_> )  |__\n"
        "|___|___|  /__|  \____/|__|  |__|_|  (____  /____/____|   \____/ \____/|____/\n"
        "         \/                        \/     \/                                 \n"
    )


@bot.event
async def on_ready():
    logger.info("InformalPool is Ready!")


@bot.event
async def on_command_error(ctx: discord.ext.commands.Context, error):
    logger.error(error)
    if type(error) == discord.ext.commands.errors.MissingRequiredArgument:
        await ctx.send(f"Error: {error} Use ``!help {ctx.command}`` for usage")
    else:
        await ctx.send(f"Error: {error}")


if __name__ == "__main__":
    motd()
    bot.add_cog(ht_cog())
    bot.add_cog(sho_cog())
    bot.add_cog(censys_cog())
    bot.add_cog(crtsh_cog())
    bot.add_cog(yellow_cog())
    bot.run(token)
