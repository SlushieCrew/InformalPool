import discord
import requests

from discord.ext import commands
from loguru import logger as log

from ..Modules._misc import misc
from ..Modules._validate import validation


class sho_cog(commands.Cog):
    def __init__(self):
        self._get = requests.get
        self.valid = validation()
        self.misc = misc()
        log.info('Loaded Shodan')


    @commands.command()
    async def honeypot(self, ctx, domain: str, detect_score=0.5) -> str:
        """
        honeypot - detect if system is a honeypot

        Args:
            domain (str): [domain to check if is a honeypot]
            detect_score (float, optional): what score should classify as honeypot. Defaults to 0.5.

        Returns:
            str: [result of detection]
        """
        url = f"https://api.shodan.io/labs/honeyscore/{self.misc.get_ip(self.valid.validate_domain(domain))}?key=Hgqwf9dHMIE157PNCeqVJc6TVvlyGKiP"
        score = self._get(url).text
        if float(score) >= detect_score:
            await self.misc.bot_send(ctx,f"{score} - Does NOT look like a real system!!!",lang="inline")

        if float(score) <= detect_score:
            await self.misc.bot_send(ctx,f"{score} - Looks like a real system!", lang="inline")
