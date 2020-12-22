# https://censys.io/ipv4/81.4.107.68/raw
# https://censys.io/domain?q=vg.no
# https://censys.io/certificates?q=vg.no

import requests
import discord
import random

from os import environ
from loguru import logger
from discord.ext import commands

from InformalPool.validate import validation
from InformalPool.misc import misc


class censys_cog(commands.Cog):
    def __init__(self):
        self._get = requests.get
        self.valid = validation()
        self.misc = misc()

    @commands.command()
    async def ipv4(self, ctx: discord.ext.commands.Context, domain: str):
        url = f"https://censys.io/ipv4/{self.valid.validate_ip(ip)}/raw"
        misc.bot_send(self._get(url).text, "json")
