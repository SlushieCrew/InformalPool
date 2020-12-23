import discord

from discord.ext import commands
from loguru import logger as log

from ..Modules._Utility import _Utility
from ..Modules._Validate import _Validate


class _Template(commands.Cog):
    def __init__(self):
        self._load_cog = True  # if cog should be loaded on startup
        self.valid = _Validate()
        self.misc = _Utility()

    @commands.command()
    async def _command_name(self, ctx, domain: str):
        """
        _command_name You want to use docstrings as theese will show up in the help menu (get the docstring generator pkg in vscode)

        ctx is needed for the bot context
        misc.bot_send is a custom function to format data in a specific way, should be implemented to see this by itself rather than static if.
        """
        output = "Hello World"
        # ...
        await self.misc.bot_send(ctx, output, lang="json")
