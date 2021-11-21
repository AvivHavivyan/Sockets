import msvcrt
import select
import socket
import sys

client_socket = socket.socket()
client_socket.connect(("127.0.0.1", 5555))
# name = input()
# client_socket.send(name.encode())
# message = client_socket.recv(1024).decode()
clients_sockets = []
message = b""
while True:
    rlist, wlist, xlist = select.select([client_socket], [client_socket], [])

    for sockets in rlist:
        if sockets == client_socket:
            msg = client_socket.recv(1024)
            print(msg.decode())
    for sockets in wlist:
        if msvcrt.kbhit():
            key = msvcrt.getch()
            print(key.decode())
            if key == b"\r":
                if message == "":
                    client_socket.close()
                else:
                    if client_socket in wlist:
                        client_socket.send(message)
                        message = b""
                        print("")
            else:
                message += key
        # if sockets == client_socket:
        #     print("reading data from user...")
            # message = sys.stdin.readline()
            # client_socket.send(message.encode())
            # # sys.stdout.write("<You>")
            # sys.stdout.flush()




