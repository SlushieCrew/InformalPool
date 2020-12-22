import discord
import requests


from loguru import logger as log
from discord.ext import commands

from InformalPool.validate import validation
from InformalPool.misc import misc


class crt_sh_cog(commands.Cog):
    def __init__(self):
        self._get = requests.get
        self.valid = validation()
        self._pd = pd.read_html
        self._unique_domains = list()
        self.headers = {
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Safari/605.1.15"
        }
        self.misc = misc()

    @commands.command()
    async def subdomains(self, domain: str) -> list[str]:
        """
        subdomains

        Args:
            domain (str): [domain to search crt records]

        Returns:
            list[str]: [returns a list of domains]
        """

        del self._unique_domains
        url = f"https://crt.sh/json?q={self.valid.validate_domain(domain)}"
        for domain in requests.get(url).json():
            for u_domain in domain["name_value"].rsplit():
                if u_domain not in self._unique_domains:
                    self.valid.validate_domain(dom)
                    self._unique_domains.append(u_domain)
        misc.bot_send(self._unique_domains, "json")
