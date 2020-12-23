import requests
import socket
import discord
import json

from discord.ext import commands

from ._validate import validation

class misc:
    def __init__(self):
        self._get = requests.get
        self.valid = validation()

    def motd(self) -> str:
        """ Gotta need a fancy motd """
        return(
            ".___        _____                           .__ __________             .__   \n"
            "|   | _____/ ____\___________  _____ _____  |  |\______   \____   ____ |  |  \n"
            "|   |/    \   __\/  _ \_  __ \/     \\__   \ |  | |     ___/  _ \ /  _ \|  |  \n"
            "|   |   |  \  | (  <_> )  | \/  Y Y  \/ __ \|  |_|    |  (  <_> |  <_> )  |__\n"
            "|___|___|  /__|  \____/|__|  |__|_|  (____  /____/____|   \____/ \____/|____/\n"
            "         \/                        \/     \/                                 \n"
        )

    def _json_pretty(self, data: dict) -> dict:
        return json.dumps(data, indent=4)

    def get_ip(self, domain: str):
        return socket.gethostbyname(domain)

    async def bot_send(self, ctx, data, lang=""):
        if lang == "txt":
            await ctx.send(f"{data}")
        elif lang == "inline":
            await ctx.send(f"``{data}``")
        else:
            try:
                await ctx.send(f"```{lang}\n{data}\n```")
            except Exception as error:
                await ctx.send(f"{error}")
