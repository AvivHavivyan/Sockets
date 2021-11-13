import socket
from dnslib import DNSRecord
import dnslib

DNS_SERVER_IP = '127.0.0.1'
DNS_SERVER_PORT = 53
DEFAULT_BUFFER_SIZE = 1024


def dns_udp_server(ip, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((ip, port))
    print("server started")
    while True:
        try:
            data, addr = server_socket.recvfrom(DEFAULT_BUFFER_SIZE)
            response = dns_handler(data, addr)
            print(response)
            print(addr)
            server_socket.sendto(response, addr)
        except Exception as ex:
            print("exception! %s" % str(ex), )


def dns_handler(data, addr):
    d = DNSRecord.parse(data)
    data = str(d)

    if data.find("www.google.com") != -1:
        response = DNSRecord(dnslib.DNSHeader(qr=1, aa=1, ra=1), q=dnslib.DNSQuestion("google.com"),
                             a=dnslib.RR("www.google.com", rdata=dnslib.A("40.70.143.2"), ttl=3))
        print(response)
        response = response.pack()
        # response = b"\xb4\x2e\x99\xf1\x07\x4a\x10\x5a\xf7\x74\x74\xa1\x08\x00\x45\x00" \
        #            b"\x00\x4c\x09\x31\x00\x00\x77\x11\xbd\xfa\x08\x08\x04\x04\x0a\x64" \
        #            b"\x66\x06\x00\x35\xc0\x18\x00\x38\xa2\x95\x75\xfe\x81\x80\x00\x01" \
        #            b"\x00\x01\x00\x00\x00\x00\x03\x77\x77\x77\x06\x67\x6f\x6f\x67\x6c" \
        #            b"\x65\x03\x63\x6f\x6d\x00\x00\x01\x00\x01\xc0\x0c\x00\x01\x00\x01" \
        #            b"\x00\x00\x01\x2c\x00\x04\xb0\x0d\x45\x3f"
        # s = """
        #         play.google.com: type A, class IN, addr 142.250.184.238
        #         Name: play.google.com
        #         Type: A (Host Address) (1)
        #         Class: IN (0x0001)
        #         Time to live: 300 (5 minutes)
        #         Data length: 4
        #         Address: 212.143.70.40
        # """
        print(addr)
        print(d)
        return response


def main():
    print("starting")
    dns_udp_server(DNS_SERVER_IP, DNS_SERVER_PORT)


if __name__ == '__main__':
    main()
