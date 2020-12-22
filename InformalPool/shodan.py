import discord
import requests

from discord.ext import commands

from InformalPool.validate import validation
from InformalPool.misc import misc


class sho_cog(commands.Cog):
    def __init__(self):
        self._get = requests.get
        self.valid = validation()
        self.misc = misc()

    @commands.command()
    async def honeypot(self, domain: str, detect_score=0.5) -> str:
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
            self.misc.bot_send(f"{score} - Does NOT look like a real system!!!")

        if float(score) <= detect_score:
            self.misc.bot_send(f"{score} - Looks like a real system!")
