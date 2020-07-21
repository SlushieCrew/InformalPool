import requests
import re

from typing import List


class validation:
    def __init__(self):
        self.online_domains = []
        self.offline_domains = []
        self._get = requests.get

    def __str__(self):
        pass

    def __repr__(self):
        pass

    def validate_ip(self, ip: str) -> str:
        pattern = re.compile(
            r"^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
        )
        if pattern.match(ip):
            return ip
        else:
            raise ValueError("Not a valid IP!")

    def validate_domain(self, domain: str) -> str:
        pattern = re.compile(
            r"(http://|https://|)(?:[A-Za-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+[a-z0-9][a-z0-9-]{0,61}[a-z0-9]"
        )
        if pattern.match(domain):
            return domain
        else:
            raise NameError("Not a Valid Domain")

    def validate_phonenumber(self, phonenumber: str) -> str:
        pattern = re.compile(
            r"(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+[a-z0-9][a-z0-9-]{0,61}[a-z0-9]"
        )
        if pattern.match(phonenumber):
            return phonenumber
        else:
            raise ValueError("Not a Valid phonenumber")

    # TODO: make a proper validation function as this is not working as intended
    def validate_live_domain(self, domain: List[str]):
        for dom in domain:
            try:
                if self._get(f"https://{dom}", verify=False).ok:
                    self.online_domains.append(dom)
                else:
                    self.offline_domains.append(dom)
            except Exception:
                pass

            return (self.online_domains, self.offline_domains)
