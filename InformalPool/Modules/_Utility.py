import requests
import socket
import discord
import os
import json
import textwrap

from loguru import logger as log
from discord.ext import commands

from ._Validate import _Validate


class _Utility:
    def __init__(self):
        self._get = requests.get
        self.valid = _Validate()

    def trunk_output(self, output: str):
        return textwrap.shorten(output, width=97, placeholder=" }")

    def motd(self) -> str:
        """ Gotta need a fancy motd """
        return (
            ".___        _____                           .__ __________             .__   \n"
            "|   | _____/ ____\___________  _____ _____  |  |\______   \____   ____ |  |  \n"
            "|   |/    \   __\/  _ \_  __ \/     \\__   \ |  | |     ___/  _ \ /  _ \|  |  \n"
            "|   |   |  \  | (  <_> )  | \/  Y Y  \/ __ \|  |_|    |  (  <_> |  <_> )  |__\n"
            "|___|___|  /__|  \____/|__|  |__|_|  (____  /____/____|   \____/ \____/|____/\n"
            "         \/                        \/     \/                                 \n"
        )

    def _json_pretty(self, data: dict) -> dict:
        return json.dumps(data, indent=4)

    # TODO: What was the meaning with this ?
    def access_control_list(self, roles: list) -> str:
        ...

    def get_ip(self, domain: str) -> str:
        return socket.gethostbyname(domain)

    # TODO: misc bot_send to detect the type of text and split the length into multiple messages
    # TODO: create custom function for embeds
    # TODO: find better way of trunking message.. this is hacky and shitty ghetto
    async def bot_send(self, ctx, data, lang="") -> str:
        trunk = 90
        if lang == "txt":
            await ctx.send(f"{ctx.author.mention}\n{data}")
        elif lang == "inline":
            await ctx.send(f"{ctx.author.mention}\n``{data}``")
        elif lang == "json":
            if len(data) > trunk:
                await ctx.send(
                    f"{ctx.author.mention}\n```json\n{self.trunk_output(self._json_pretty(data))}\n```"
                )
            else:
                await ctx.send(
                    f"{ctx.author.mention}\n```json\n{(self._json_pretty(data))}\n```"
                )
        else:
            try:
                if len(data) > trunk:
                    await ctx.send(
                        f"{ctx.author.mention}\n```{lang}\n{self.trunk_output(data)}\n```"
                    )
                await ctx.send(f"{ctx.author.mention}\n```{lang}\n{data}\n```")

            except Exception as error:
                await ctx.send(f"{error}")

    def _noload_cog(self):
        """Don't load this cog"""
        # TODO: respect the class variables set in each cog, to load or not load the cog.
        ...
