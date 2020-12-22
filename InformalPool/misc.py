import requests
import socket
import discord

from InformalPool.validate import validation


class misc:
    def __init__(self):
        self._get = requests.get
        self.valid = validation()

    def _json_pretty(self, data: dict) -> dict:
        return json.dumps(data, indent=4)

    def get_ip(self, domain: str):
        return socket.gethostbyname(domain)

    async def bot_send(command:str, lang:str=""):
        try:
            await ctx.send(self.discord_format(command, lang=lang))
        except Exception as error:
            await ctx.send(f"{error}")

    def discord_format(text_str: str, lang="") -> str:
        # if one line use double
        # if multiple lines use tripple
        # if msg is longer than 1.5k word split
        # if msg is longer than 3k words break.. as that's more than two whole messages!
        return f"```{lang}\n{text_str}\n```"
