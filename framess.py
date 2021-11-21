from scapy.all import *
from scapy.layers.l2 import Ether
#
# frames = sniff(count=2)
# frame = frames[0]

MY_ADDRESS = "b4:2e:99:f1:07:4a"


def filter_mac(frame):
    return (Ether in frame) and (frame[Ether].dst == MY_ADDRESS)


def print_source_address(frame):
    print(frame[Ether].src)


frames = sniff(count=2, lfilter=filter_mac, prn=print_source_address)
frames.show()
