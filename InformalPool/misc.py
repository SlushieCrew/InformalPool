import requests
import socket

from InformalPool.validate import validation


class misc:
    def __init__(self):
        self._get = requests.get
        self.valid = validation()

    def detect_robots_txt(self, url: str) -> str:
        # check for robots txt files
        pass

    def detect_random_fucking_shit(self, url: str) -> str:
        # just check all random fucking things !
        pass

    def get_ip(self, domain: str):
        return socket.gethostbyname(domain)

    async def bot_send(command:str, lang:str=""):
        try:
            await ctx.send(self.discord_format(command, lang=lang))
        except Exception as error:
            await ctx.send(f"{error}"

    def discord_format(text_str: str, lang="") -> str:
        """
        discord_format [summary]

        Args:
            text_str (str): text to insert between a codeblock
            lang (str, optional): [pick a programming language to get syntax highligth]. Defaults to "".

        Returns:
            str: [description]
        """
        return f"```{lang}\n{text_str}\n```"
