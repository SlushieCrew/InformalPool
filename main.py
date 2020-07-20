from InformalPool.hacker_target import hacker_target
from InformalPool.shodan import shodan

ht = hacker_target()
sho = shodan()

# FAAAAST as fuck port scan (prob cached, but still!)
print (ht.port_scan('8.8.8.8'))

# we got honey ;)
print (sho.honeypot_detect('8.8.8.8'))