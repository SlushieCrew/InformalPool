import discord

from discord.ext import commands
from loguru import logger as log

from ..Modules._Utility import _Utility
from ..Modules._Validate import _Validate

# https://github.com/sherlock-project/sherlock/blob/master/sherlock/sherlock.py#L611-L618


class Sherlock(commands.Cog):
    def __init__(self):
        self._load_cog = False
        self.valid = _Validate()
        self.utility = _Utility()

    @commands.command()
    async def sherlock(self, ctx, domain: str):
        output = "Work in progress"
        await self.utility.bot_send(ctx, output, lang="txt")
