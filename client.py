import socket
import urllib
import re

my_socket = socket.socket()
my_socket.connect(("127.0.0.1", 80))
is_exit = False

message = input()
length = str(len(message)).zfill(4)
enc_message = str(length) + message
my_socket.send(enc_message.encode())
print(enc_message)

if message[0:3] == "GET":
    data = my_socket.recv(4096).decode()
    # length_start = data.find('Content-Length: ') + 16
    # length_end = data.find('\r\n', length_start)
    # content_length = data[length_start:length_end]
    # content_start = data.find('\r\n\r\n') + 4
    # header_length = length_start
    match = re.search('Content-Length: (\\d*)', data)
    content_length = match.groups()[0]
    remainder = int(content_length)
    data += my_socket.recv(remainder).decode()
    print(data)
