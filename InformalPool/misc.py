import requests
import socket

from InformalPool.validate import validation


class misc:
    def __init__(self):
        self._get = requests.get
        self.valid = validation()

    def __str__(self):
        pass

    def __repr__(self):
        pass

    def detect_robots_txt(self, url: str) -> str:
        # check for robots txt files
        pass

    def detect_random_fucking_shit(self, url: str) -> str:
        # just check all random fucking things !
        pass

    def get_ip(self, domain: str):
        return socket.gethostbyname(domain)