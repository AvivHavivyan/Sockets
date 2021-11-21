import msvcrt
import select
import socket

client_socket = socket.socket()
client_socket.connect(("127.0.0.1", 5555))
name = input()
client_socket.send(name.encode())
# message = client_socket.recv(1024).decode()
clients_sockets = []
rlist, wlist, xlist = select.select([client_socket], [client_socket], [])
message = b""
while True:
    if msvcrt.kbhit():
        key = msvcrt.getch()
        if key == b"\r":
            if message == "":
                client_socket.close()
            else:
                for cur in wlist:
                    if cur == client_socket:
                        msg = client_socket.send(message)
                message = b""
        else:
            message += key
    for cur in rlist:
        print("test")
        if cur == client_socket:
            msg = client_socket.recv(1024)
            print(msg.decode())


