import requests
import re


class _Validate:
    def __init__(self):
        self.online_domains = []
        self.offline_domains = []
        self._get = requests.get

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
            r"(http://|https://|)(?:[\*A-Za-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+[a-z0-9][a-z0-9-]{0,61}[a-z0-9]"
        )
        if pattern.match(str(domain)):
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
