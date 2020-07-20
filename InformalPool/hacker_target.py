import requests
import re

class hacker_target:
    def __init__(self):
        self._get = requests.get
        self.root_url =  "https://api.hackertarget.com/"

    def __str__(self):
        pass

    def __repr__(self):
        pass

    # It's okay to use regex to validate ip's  :)
    def validate_ip(self, ip:str) -> str:
        pattern = re.compile(r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$')
        if (pattern.match(ip)):
            return (ip)
        else:
            raise ValueError('Not a valid IP!')

    def mtr_tracert(self, ip:str) -> str:
        """ Access to the MTR Traceroute API """
        url = f"https://api.hackertarget.com/mtr/?q={self.validate_ip(ip)}"
        return (self._get(url).text)

    def nping(self, ip:str) -> str:
        """ Access to the on-line Test Ping API """
        url = f"https://api.hackertarget.com/nping/?q={self.validate_ip(ip)}"
        return (self._get(url).text)

    # Used in ReconDog
    def dns_lookup(self, ip:str) -> str:
        """ Access to the DNS Lookup API """
        url = f"https://api.hackertarget.com/dnslookup/?q={self.validate_ip(ip)}"
        return (self._get(url).text)

    def reverse_dns_lookup(self, ip:str) -> str:
        """ Access to the Reverse DNS Lookup API """
        url = f"https://api.hackertarget.com/reversedns/?q={self.validate_ip(ip)}"
        return (self._get(url).text)

    # Used in ReconDog
    def whois_lookup(self, ip:str) -> str:
        """ Access to the Whois Lookup API """
        url = f"https://api.hackertarget.com/whois/?q={self.validate_ip(ip)}"
        return (self._get(url).text)


    def geoip_lookup(self, ip:str) -> str:
        """ Access to the GeoIP Lookup API """
        url = f"https://api.hackertarget.com/geoip/?q={self.validate_ip(ip)}"
        return (self._get(url).text)

    def host_search(self, ip:str) -> str:
        url = f"https://api.hackertarget.com/hostsearch/?q={self.validate_ip(ip)}"
        return (self._get(url).text)

    def zone_lookup(self, ip:str) -> str:
        url = f"https://api.hackertarget.com/zonetransfer/?q={ip}"
        return (self._get(url).text)

    # Used in ReconDog
    def reverse_ip_lookup(self, ip:str) -> str:
        """ Access to the Reverse IP Lookup API """
        url = f"https://api.hackertarget.com/reverseiplookup/?q={self.validate_ip(ip)}"
        return (self._get(url).text)

    def http_headers(self, domain:str) -> str:
        """ Access to the HTTP Headers API """
        url = f"https://api.hackertarget.com/httpheaders/?q={domain}"
        return (self._get(url).text)

    def pagelinks(self, domain:str) -> str:
        """ Access to the Page Links API """
        url = f"https://api.hackertarget.com/pagelinks/?q={domain}"
        return (self._get(url).text)

    def as_lookup(self, ip:str) -> str:
        """ Access to the AS Lookup API """
        url = f"https://api.hackertarget.com/aslookup/?q={self.validate_ip(ip)}"
        return (self._get(url).text)

    def find_shared_dns(self, ip:str) -> str:
        url = f"https://api.hackertarget.com/findshareddns/?q={self.validate_ip(ip)}"
        return (self._get(url).text)

    # Used in ReconDog
    def port_scan(self, ip:str) -> str:
        url = f"http://api.hackertarget.com/nmap/?q={self.validate_ip(ip)}"
        return (self._get(url).text)