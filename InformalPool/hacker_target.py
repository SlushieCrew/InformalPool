import requests
import discord
import re

from discord.ext import commands

from InformalPool.validate import validation
from InformalPool.misc import misc


class ht_cog(commands.Cog):
    def __init__(self):
        self._get = requests.get
        self.valid = validation()
        self.misc = misc()

    def __str__(self):
        return f"HackerTarget {self.__class__}"

    @commands.command()
    def mtr_tracert(self, domain: str) -> str:
        """ Access to the MTR Traceroute API """
        url = f"https://api.hackertarget.com/mtr/?q={self.misc.get_ip(self.valid.validate_domain(domain))}"
        self.misc.bot_send(self.misc._json_pretty(self._get(url).text), "json")

    @commands.command()
    def nping(self, domain: str) -> str:
        """ Access to the on-line Test Ping API """
        url = f"https://api.hackertarget.com/nping/?q={self.misc.get_ip(self.valid.validate_domain(domain))}"
        self.misc.bot_send(self.misc._json_pretty(self._get(url).text), "json")

    @commands.command()
    def dns_lookup(self, domain: str) -> str:
        """ Access to the DNS Lookup API """
        url = f"https://api.hackertarget.com/dnslookup/?q={self.misc.get_ip(self.valid.validate_domain(domain))}"
        self.misc.bot_send(self.misc._json_pretty(self._get(url).text), "json")

    @commands.command()
    def reverse_dns_lookup(self, domain: str) -> str:
        """ Access to the Reverse DNS Lookup API """
        url = f"https://api.hackertarget.com/reversedns/?q={self.misc.get_ip(self.valid.validate_domain(domain))}"
        self.misc.bot_send(self.misc._json_pretty(self._get(url).text), "json")

    @commands.command()
    def whois_lookup(self, domain: str) -> str:
        """ Access to the Whois Lookup API """
        url = f"https://api.hackertarget.com/whois/?q={self.misc.get_ip(self.valid.validate_domain(domain))}"
        self.misc.bot_send(self.misc._json_pretty(self._get(url).text), "json")

    @commands.command()
    def geoip_lookup(self, domain: str) -> str:
        """ Access to the GeoIP Lookup API """
        url = f"https://api.hackertarget.com/geoip/?q={self.misc.get_ip(self.valid.validate_domain(domain))}"
        self.misc.bot_send(self.misc._json_pretty(self._get(url).text), "json")

    @commands.command()
    def host_search(self, domain: str) -> str:
        url = f"https://api.hackertarget.com/hostsearch/?q={self.misc.get_ip(self.valid.validate_domain(domain))}"
        self.misc.bot_send(self.misc._json_pretty(self._get(url).text), "json")

    @commands.command()
    def zone_lookup(self, domain: str) -> str:
        url = f"https://api.hackertarget.com/zonetransfer/?q={self.misc.get_ip(self.valid.validate_domain(domain))}"
        self.misc.bot_send(self.misc._json_pretty(self._get(url).text), "json")

    @commands.command()
    def reverse_ip_lookup(self, domain: str) -> str:
        """ Access to the Reverse IP Lookup API """
        url = f"https://api.hackertarget.com/reverseiplookup/?q={self.misc.get_ip(self.valid.validate_domain(domain))}"
        self.misc.bot_send(self.misc._json_pretty(self._get(url).text), "json")

    @commands.command()
    def http_headers(self, domain: str) -> str:
        """ Access to the HTTP Headers API """
        url = f"https://api.hackertarget.com/httpheaders/?q={self.valid.validate_domain(domain)}"
        self.misc.bot_send(self.misc._json_pretty(self._get(url).text), "json")

    @commands.command()
    def pagelinks(self, domain: str) -> str:
        """ Access to the Page Links API """
        url = f"https://api.hackertarget.com/pagelinks/?q={self.valid.validate_domain(domain)}"
        self.misc.bot_send(self.misc._json_pretty(self._get(url).text), "json")

    @commands.command()
    def as_lookup(self, domain: str) -> str:
        """ Access to the AS Lookup API """
        url = f"https://api.hackertarget.com/aslookup/?q={self.misc.get_ip(self.valid.validate_domain(domain))}"
        self.misc.bot_send(self.misc._json_pretty(self._get(url).text), "json")

    @commands.command()
    def find_shared_dns(self, domain: str) -> str:
        url = f"https://api.hackertarget.com/findshareddns/?q={self.misc.get_ip(self.valid.validate_domain(domain))}"
        self.misc.bot_send(self.misc._json_pretty(self._get(url).text), "json")

    @commands.command()
    def port_scan(self, domain: str) -> str:
        url = f"http://api.hackertarget.com/nmap/?q={self.misc.get_ip(self.valid.validate_domain(domain))}"
        self.misc.bot_send(self.misc._json_pretty(self._get(url).text), "json")
