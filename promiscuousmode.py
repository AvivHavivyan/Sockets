from scapy.all import *
from scapy.layers.l2 import ARP, Ether

# packet = Ether(dst="ff:ff:ff:ff:ff:ff", src="b4:2e:99:f1:07:4a")/ARP(
#     hwtype=0x01, ptype=0x0800, hwlen=0x06, plen=0x04, op=0x01,
#     hwsrc="b4:2e:99:f1:07:4a", psrc="10.100.102.7",
#     hwdst="00:00:00:00:00:00", pdst="10.0.2.13")
# packets = [Ether(dst=ETHER_BROADCAST) / ARP(op=1, psrc="10.100.102.7", pdst="10.0.2.13", hwdst=ETHER_BROADCAST)]
# resp = sendp(packets)
# resp.show()
packet = Ether(dst='ff:ff:ff:ff:ff:fe')/ARP(pdst='10.100.102.13')
packet.show()


# while True:
response = srp1(packet, promisc=True)
# response = sendp(packet)
# if response is not None:
response.show()
# break

