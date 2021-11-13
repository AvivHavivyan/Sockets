import socket
import datetime
import glob
import shutil
import os
import subprocess

is_closed = False
server_socket = socket.socket()
server_socket.bind(("0.0.0.0", 8820))
server_socket.listen()
print("Server is up")

while not is_closed:
    (client_socket, client_address) = server_socket.accept()
    print("Connected")
    while True:
        length = client_socket.recv(4).decode()
        if length.isnumeric() and length is not None:
            message = client_socket.recv(int(length)).decode()
            if message[0:4] == "copy":
                path = message.split(" ", 2)

                if os.path.exists(path[1]) and not os.path.exists(path[2]):
                    shutil.copy(path[1], path[2])
                    client_socket.send(b'File copied successfully')

                if os.path.exists(path[2]):
                    client_socket.send(b'File name taken')
                else:
                    client_socket.send(b'No such file or directory')

            if message[0:7] == "execute":
                path = message.split(" ", 1)
                subprocess.call(path[1])
                client_socket.send(b'Opening...')

            if message[0:3] == "dir":
                path = message.split(" ", 1)
                files_list = glob.glob(path[1] + "\\*")
                client_socket.send(str(files_list).encode())

            if message == "time":
                message = str(datetime.datetime.now())
                client_socket.send(message.encode())

            if message == "exit":
                exit_message = "Closing client socket..."
                client_socket.send(exit_message.encode())
                client_socket.close()
                break

            if message == "close server":
                print("Closing...")
                client_socket.close()
                server_socket.close()
                print("Server closed")
                is_closed = True
                break
        else:
            message = "Invalid command"
            client_socket.send(message.encode())


