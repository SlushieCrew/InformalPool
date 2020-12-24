# https://censys.io/ipv4/81.4.107.68/raw
# https://censys.io/domain?q=vg.no
# https://censys.io/certificates?q=vg.no

import requests
import discord

from discord.ext import commands
from loguru import logger as log

from ..Modules._Utility import _Utility
from ..Modules._Validate import _Validate


class Censys(commands.Cog):
    def __init__(self):
        self._load_cog = False
        self._get = lambda url: requests.get(url)
        self.valid = _Validate()
        self.utility = _Utility()

    @commands.command()
    async def ipv4(self, ctx, domain: str):
        url = f"https://censys.io/ipv4/{self.valid.validate_ip(ip)}/raw"

        await self._Utility.bot_send(ctx, self._get(url).json(), lang="json")
