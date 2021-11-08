import socket
my_socket = socket.socket()
my_socket.connect(("127.0.0.1", 8820))
is_exit = False

while not is_exit:
    message = input()
    length = str(len(message)).zfill(4)
    enc_message = str(length) + message
    my_socket.send(enc_message.encode())
    data = my_socket.recv(1024).decode()
    if message == "time":
        print(data)
    if message == "exit":
        my_socket.close()
        print(data)
        is_exit = True
        break
    if message[0:3] == "dir":
        dirs = data.split(", ")
        print(*dirs, sep="\n ")
    if message[0:7] == "execute":
        print(data)
    if message[0:4] == "copy":
        print(data)
    if message == "close server":
        print("Server closed, exiting the program.")

        break
