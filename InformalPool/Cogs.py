import discord
import random

from os import environ
from loguru import logger
from discord.ext import commands

from InformalPool.hacker_target import hacker_target
from InformalPool.shodan import shodan
from InformalPool.crt_sh import crt_sh
from InformalPool.misc import misc
from InformalPool.yellowpages_no import yellowpages


<<<<<<< HEAD
=======
class censys_cog(commands.Cog):
    def __init__(self):
        self.censys = censys()

    @commands.command()
    async def ipv4(self, ctx: discord.ext.commands.Context, domain: str):
        try:
            await ctx.send(f"```{self.censys.ipv4(misc().get_ip(domain))}```")
        except Exception as error:
            await ctx.send(f"{error}")


>>>>>>> 74ee7d07a0f73372ae31e770e0d3400e9ddb33f0
class crtsh_cog(commands.Cog):
    def __init__(self):
        self.crt_sh = crt_sh()

    @commands.command()
    async def subdomains(self, ctx: discord.ext.commands.Context, domain: str):
        try:
            await ctx.send(f"```{self.crt_sh.find_subdomains(domain)}```")
        except Exception as error:
            await ctx.send(f"{error}")


class sho_cog(commands.Cog):
    def __init__(self):
        self.sho = shodan()

    @commands.command()
    async def honeypot(self, ctx: discord.ext.commands.Context, str):
        try:
            await ctx.send(
                f"```{self.sho.honeypot_detect(misc().get_ip(domain))}```"
            )
        except Exception as error:
            await ctx.send(f"{error}")


class ht_cog(commands.Cog):
    def __init__(self):
        self.ht = hacker_target()

    @commands.command()
    async def port_scan(
        self,
        ctx: discord.ext.commands.Context,
        domain: str,
    ):

        try:
            await ctx.send(f"```{self.ht.port_scan(misc().get_ip(domain))}```")
        except Exception as error:
            await ctx.send(f"{error}")

    @commands.command()
    async def MTR_tracert(
        self,
        ctx: discord.ext.commands.Context,
        domain: str,
    ):
        """ Access to the MTR Traceroute API """

        try:
            await ctx.send(f"```{self.ht.mtr_tracert(misc().get_ip(domain))}```")
        except Exception as error:
            await ctx.send(f"{error}")

    @commands.command()
    async def dns_lookup(
        self,
        ctx: discord.ext.commands.Context,
        domain: str,
    ):
        """ Access to the DNS Lookup API """

        try:
            await ctx.send(f"```{self.ht.dns_lookup(misc().get_ip(domain))}```")
        except Exception as error:
            await ctx.send(f"{error}")

    @commands.command()
    async def whois_lookup(
        self,
        ctx: discord.ext.commands.Context,
        domain: str,
    ):
        """ Access to the Whois Lookup API """

        try:
            await ctx.send(f"```{self.ht.whois_lookup(misc().get_ip(domain))}```")
        except Exception as error:
            await ctx.send(f"{error}")

    @commands.command()
    async def reverse_ip_lookup(
        self,
        ctx: discord.ext.commands.Context,
        domain: str,
    ):
        """ Access to the Reverse IP Lookup API """

        try:
            await ctx.send(
                f"```{self.ht.reverse_ip_lookup(misc().get_ip(domain))}```"
            )
        except Exception as error:
            await ctx.send(f"{error}")

    @commands.command()
    async def http_headers(
        self,
        ctx: discord.ext.commands.Context,
        domain: str,
    ):
        """ Access to the HTTP Headers API """

        try:
            await ctx.send(f"```{self.ht.http_headers(misc().get_ip(domain))}```")
        except Exception as error:
            await ctx.send(f"{error}")


class yellow_cog(commands.Cog):
    """ Yellowpages Norway """

    def __init__(self):
        self.yellow = yellowpages()

    @commands.command()
    async def check_phonenumber(
        self, ctx: discord.ext.commands.Context, search_query: str
    ):
        try:
            await ctx.send(f"```{self.yellow.check_phonenumber(search_query)}```")
        except Exception as error:
            await ctx.send(f"{error}")


# nping
# reverse_dns_lookup
# geoip_lookup
# host_search
# zone_lookup
# http_headers
# pagelinks
# as_lookup
# find_shared_dns


class misc_cog(commands.Cog):
    @commands.command()
    async def get_ip(self, ctx: discord.ext.commands.Context, domain: str):
        try:
            await ctx.send(f"```{misc().get_ip(domain)}```")
        except Exception as error:
            await ctx.send(f"{error}")
