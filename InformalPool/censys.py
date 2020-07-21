# https://censys.io/ipv4/81.4.107.68/raw
# https://censys.io/domain?q=vg.no
# https://censys.io/certificates?q=vg.no

import requests
from InformalPool.validate import validation


class censys:
    def __init__(self):
        self._get = requests.get
        self.valid = validation()

    def __str__(self):
        pass

    def __repr__(self):
        pass

    def ipv4(self, ip: str):
        url = f"https://censys.io/ipv4/{self.valid.validate_ip(ip)}/raw"
        print(self._get(url).text)
