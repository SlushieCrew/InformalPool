import requests

class hacker_target:
    def __init__(self):
        self._get = requests.get
        self.root_url =  "https://api.hackertarget.com/"

    def __str__(self):
        pass

    def __repr__(self):
        pass

    def mtr_tracert():
        """
        Access to the MTR Traceroute API

        https://api.hackertarget.com/mtr/?q=8.8.8.8
        """
        pass

    def nping():
        """
        Access to the on-line Test Ping API

        https://api.hackertarget.com/nping/?q=8.8.8.8
        """
        pass

    # Used in ReconDog
    def dns_lookup():
        """
        Access to the DNS Lookup API

        https://api.hackertarget.com/dnslookup/?q=google.com
        """
        pass

    def reverse_dns_lookup():
        """
        Access to the Reverse DNS Lookup API

        https://api.hackertarget.com/reversedns/?q=8.8.8.8
        """
        pass

    # Used in ReconDog
    def whois_lookup():
        """
        Access to the Whois Lookup API

        https://api.hackertarget.com/whois/?q=8.8.8.8
        """
        pass


    def geoip_lookup():
        """
        Access to the GeoIP Lookup API

        https://api.hackertarget.com/geoip/?q=8.8.8.8
        """
        pass

    def host_search():
        """
        https://api.hackertarget.com/hostsearch/?q=8.8.8.8
        """
        pass

    def zone_lookup():
        """
        https://api.hackertarget.com/zonetransfer/?q=8.8.8.8
        """
        pass

    # Used in ReconDog
    def reverse_ip_lookup():
        """
        Access to the Reverse IP Lookup API

        https://api.hackertarget.com/reverseiplookup/?q=8.8.8.8
        """
        pass

    def http_headers():
        """
        Access to the HTTP Headers API

        https://api.hackertarget.com/httpheaders/?q=www.google.com
        """
        pass

    def pagelinks():
        """
        Access to the Page Links API

        https://api.hackertarget.com/pagelinks/?q=www.google.com
        """
        pass


    def as_lookup():
        """
        Access to the AS Lookup API

        https://api.hackertarget.com/aslookup/?q=1.1.1.1
        """
        pass

    def find_shared_dns():
        """
        https://api.hackertarget.com/findshareddns/?q=8.8.8.8
        """
        pass

    # Used in ReconDog
    def port_scan():
        """
        http://api.hackertarget.com/nmap/?q=8.8.8.8
        """
        pass