import requests
import discord
import re

from discord.ext import commands
from loguru import logger as log

from ..Modules._Utility import _Utility
from ..Modules._Validate import _Validate


class HackerTarget(commands.Cog):
    def __init__(self):
        self._load_cog = False
        self._get = lambda url: requests.get(url)
        self.valid = _Validate()
        self.utility = _Utility()

    @commands.command()
    async def ht_mtr_tracert(self, ctx, domain: str) -> str:
        """Access to the MTR Traceroute API"""
        url = f"https://api.hackertarget.com/mtr/?q={self.utility.get_ip(domain)}"
        await self.utility.bot_send(ctx, f"{(self._get(url).text)}", lang="")

    @commands.command()
    async def ht_nping(self, ctx, domain: str) -> str:
        """Access to the on-line Test Ping API"""
        url = f"https://api.hackertarget.com/nping/?q={self.utility.get_ip(domain)}"
        await self.utility.bot_send(ctx, (self._get(url).text), lang="")

    @commands.command()
    async def ht_dns_lookup(self, ctx, ip: str) -> str:
        """Access to the DNS Lookup API"""
        url = f"https://api.hackertarget.com/dnslookup/?q={ip}"
        await self.utility.bot_send(ctx, (self._get(url).text), lang="txt")

    @commands.command()
    async def ht_reverse_dns_lookup(self, ctx, domain: str) -> str:
        """Access to the Reverse DNS Lookup API"""
        url = (
            f"https://api.hackertarget.com/reversedns/?q={self.utility.get_ip(domain)}"
        )
        await self.utility.bot_send(ctx, (self._get(url).text), lang="txt")

    @commands.command()
    async def ht_whois_lookup(self, ctx, domain: str) -> str:
        """Access to the Whois Lookup API"""
        url = f"https://api.hackertarget.com/whois/?q={self.utility.get_ip(domain)}"
        await self.utility.bot_send(ctx, (self._get(url).text), lang="txt")

    @commands.command()
    async def ht_geoip_lookup(self, ctx, domain: str) -> str:
        """Access to the GeoIP Lookup API"""
        url = f"https://api.hackertarget.com/geoip/?q={self.utility.get_ip(domain)}"
        await self.utility.bot_send(ctx, (self._get(url).text))

    @commands.command()
    async def ht_host_search(self, ctx, domain: str) -> str:
        url = (
            f"https://api.hackertarget.com/hostsearch/?q={self.utility.get_ip(domain)}"
        )
        await self.utility.bot_send(ctx, (self._get(url).text), lang="inline")

    @commands.command()
    async def ht_zone_lookup(self, ctx, domain: str) -> str:
        url = f"https://api.hackertarget.com/zonetransfer/?q={self.utility.get_ip(domain)}"
        await self.utility.bot_send(ctx, (self._get(url).text), lang="txt")

    @commands.command()
    async def ht_reverse_ip_lookup(self, ctx, domain: str) -> str:
        """Access to the Reverse IP Lookup API"""
        url = f"https://api.hackertarget.com/reverseiplookup/?q={self.utility.get_ip(domain)}"
        await self.utility.bot_send(ctx, (self._get(url).text), lang="txt")

    @commands.command()
    async def ht_http_headers(self, ctx, domain: str) -> str:
        """Access to the HTTP Headers API"""
        url = f"https://api.hackertarget.com/httpheaders/?q={domain}"
        await self.utility.bot_send(ctx, (self._get(url).text), lang="")

    @commands.command()
    async def ht_pagelinks(self, ctx, domain: str) -> str:
        """Access to the Page Links API"""
        url = f"https://api.hackertarget.com/pagelinks/?q={domain}"
        if self._get(url).text == "":
            retur = "No pagelinks found"
        else:
            retur = self._get(url).text
        await self.utility.bot_send(ctx, (retur), lang="txt")

    @commands.command()
    async def ht_as_lookup(self, ctx, domain: str) -> str:
        """Access to the AS Lookup API"""
        url = f"https://api.hackertarget.com/aslookup/?q={self.utility.get_ip(domain)}"
        await self.utility.bot_send(ctx, (self._get(url).text), lang="inline")

    @commands.command()
    async def ht_find_shared_dns(self, ctx, domain: str) -> str:
        url = f"https://api.hackertarget.com/findshareddns/?q={self.utility.get_ip(domain)}"
        await self.utility.bot_send(ctx, (self._get(url).text), lang="txt")

    @commands.command()
    async def ht_port_scan(self, ctx, domain: str) -> str:
        url = f"http://api.hackertarget.com/nmap/?q={self.utility.get_ip(domain)}"
        await self.utility.bot_send(ctx, (self._get(url).text), lang="")
