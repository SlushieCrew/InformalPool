# look for subdomains in crt records.
# https://crt.sh/?q=google.no
# Matching Identities col
import requests
import pandas as pd

from InformalPool.validate import validation
from loguru import logger as log


class crt_sh:
    def __init__(self):
        self._get = requests.get
        self.valid = validation()
        self._pd = pd.read_html
        self._unique_domains = []
        self.headers = {
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Safari/605.1.15"
        }

    def __str__(self):
        pass

    def __repr__(self):
        pass

    def find_subdomains(self, domain: str) -> str:
        url = f"https://crt.sh/?q={domain}"
        _dot_ext = domain.split(".")[-1]
        site = self._get(url, headers=self.headers).text
        tr = self._pd(site)
        for domain in tr[2]["Matching Identities"]:
            domain = domain.split(_dot_ext)
            for dom in domain:
                if dom:
                    try:
                        dom = f"{dom}{_dot_ext}"
                        if dom not in self._unique_domains:
                            # log.info(f"Found domain: {dom}")
                            self.valid.validate_domain(dom)
                            self._unique_domains.append(dom)
                    except NameError as e:
                        print(f"Error: {e} - Result: {dom}")
        return self._unique_domains


"""
url = "https://cair.uia.no/other/cair-technical-meetings"
page = requests.get(url).text
df = pd.read_html(page)
"""
