from scapy.all import *
from scapy.layers.inet import IP, ICMP

x = 1
dest = "142.250.200.4"
while True:
    tracert_packet = IP(ttl=x, dst=str(dest)) / ICMP()
    response_packet = sr1(tracert_packet)
    print(response_packet[IP].src)
    if response_packet[IP].src == dest:
        print(response_packet[IP].src)

        response_packet.show()
        break
    x += 1

