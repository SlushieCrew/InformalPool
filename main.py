#!/usr/bin/env python3
from InformalPool.hacker_target import hacker_target
from InformalPool.shodan import shodan
from InformalPool.censys import censys
from InformalPool.crt_sh import crt_sh
from InformalPool.validate import validation

ht = hacker_target()
sho = shodan()
cen = censys()
cert = crt_sh()
valid = validation()

# FAAAAST as fuck port scan (prob cached, but still!)
# print(ht.pagelinks("uia.no"))

# we got honey ;)
# print(sho.honeypot_detect("8.8.8.8"))

# censyyys
# print(cen.ipv4("81.4.107.68"))


# list_of_domains = cert.find_subdomains("strava.com")
# print(list_of_domains)

import socket


def get_ip(self, domain: str):
    return socket.gethostbyname(domain)
