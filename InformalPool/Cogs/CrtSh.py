import discord
import requests

from discord.ext import commands
from loguru import logger as log
from requests.packages.urllib3.exceptions import InsecureRequestWarning

from ..Modules._Utility import _Utility
from ..Modules._Validate import _Validate

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


class CrtSh(commands.Cog):
    def __init__(self):
        self._load_cog = True
        self._get = requests.get
        self.utility = _Utility()
        self.valid = _Validate()

    def is_domain_alive(self, domain: str, timeout: int = 3):
        if "http" or "https" not in domain:
            domain = f"https://{domain}"

        try:
            if (
                requests.get(f"{domain}", timeout=timeout, verify=False).status_code
                is not False
            ):
                return domain

        except Exception:
            return False

    @commands.command()
    async def subdomain(self, ctx, domain):
        """
        subdomains

        Args:
            domain (str): [domain to search crt records]

        Returns:
            list[str]: [returns a list of domains]
        """

        _unique_domains = []
        _alive_domains = []
        url = f"https://crt.sh/json?q={domain}"
        for domain in requests.get(url).json():
            for u_domain in domain["name_value"].rsplit():
                if u_domain not in _unique_domains and "*" not in u_domain:
                    _unique_domains.append(u_domain)

        for _domain in _unique_domains:
            if self.is_domain_alive(_domain) != False:
                _alive_domains.append(_domain)

        await self.utility.bot_send(ctx, sorted(_alive_domains), lang="json")
