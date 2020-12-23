# https://censys.io/ipv4/81.4.107.68/raw
# https://censys.io/domain?q=vg.no
# https://censys.io/certificates?q=vg.no

import requests
import discord

from discord.ext import commands
from loguru import logger as log

from ..Modules._misc import misc
from ..Modules._validate import validation


class censys_cog(commands.Cog):
    def __init__(self):
        self._get = lambda url: requests.get(url)
        self.valid = validation()
        self.misc = misc()
        log.info('Loaded Censys')

    @commands.command()
    async def ipv4(self, ctx, domain: str):
        url = f"https://censys.io/ipv4/{self.valid.validate_ip(ip)}/raw"
        
        await self.misc.bot_send(ctx, self._get(url).json(), lang="json")
