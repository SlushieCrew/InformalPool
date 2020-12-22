import discord
import requests

from discord.ext import commands

from InformalPool.validate import validation
from InformalPool.misc import misc


class crtsh_cog(commands.Cog):
    def __init__(self):
        self._get = requests.get
        self.valid = validation()
        self.misc = misc()
        self.headers = {
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Safari/605.1.15"
        }

    @commands.command()
    async def subdomains(self, domain: str):
        """
        subdomains

        Args:
            domain (str): [domain to search crt records]

        Returns:
            list[str]: [returns a list of domains]
        """

        _unique_domains = []
        url = f"https://crt.sh/json?q={self.valid.validate_domain(domain)}"
        for domain in requests.get(url).json():
            for u_domain in domain["name_value"].rsplit():
                if u_domain not in _unique_domains:
                    self.valid.validate_domain(u_domain)
                    _unique_domains.append(u_domain)
        self.misc.bot_send(_unique_domains, "json")
