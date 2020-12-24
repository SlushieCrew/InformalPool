import discord
import requests

from discord.ext import commands
from loguru import logger as log

from ..Modules._Utility import _Utility
from ..Modules._Validate import _Validate


class Alienvault(commands.Cog):
    def __init__(self):
        self._load_cog = True
        self._get = lambda url: requests.get(url)
        self.valid = _Validate()
        self.utility = _Utility()

    # @commands.has_role("Infosec")
    @commands.command()
    async def passive_dns(self, ctx, domain: str):
        """
        passive_dns

        Args:
            ctx ([type]): [discord bot context]
            domain (str): [domain name]
        """
        _pointers = {}
        _response = self._get(
            f"https://otx.alienvault.com/api/v1/indicators/domain/{domain}/passive_dns"
        ).json()

        for api_response in dict(_response)["passive_dns"]:
            _addr = api_response["address"]
            _host = api_response["hostname"]
            _type = api_response["record_type"]
            _pointers[_host] = {_addr: _type}

        await self.utility.bot_send(ctx, _pointers, lang="json")
