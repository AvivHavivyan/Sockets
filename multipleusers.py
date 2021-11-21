import socket
import select

MAX_MSG_LENGTH = 1024
SERVER_PORT = 5555
SERVER_IP = "127.0.0.1"


def print_client_socket(client_sockets):
    for c in client_sockets:
        print("\t", c.getpeername())


server_socket = socket.socket()
server_socket.bind((SERVER_IP, SERVER_PORT))
server_socket.listen()
clients_sockets = []
messages_to_send = []

while True:
    rlist, wlist, xlist = select.select([server_socket] + clients_sockets, clients_sockets, [])
    for current_socket in rlist:
        if current_socket is server_socket:
            connection, client_address = current_socket.accept()
            print("New client joined!")
            clients_sockets.append(connection)
            print_client_socket(clients_sockets)
        else:
            print("Data from existing connection \n")

            data = current_socket.recv(MAX_MSG_LENGTH).decode()
            print(data)
            if data == "":
                print("Connection closed")
                clients_sockets.remove(current_socket)
                current_socket.close()
                print_client_socket(clients_sockets)
            else:
                messages_to_send.append((current_socket, data))
        for message in messages_to_send:
            current_socket, data = message
            clients_to_send = clients_sockets.copy()
            clients_to_send.remove(current_socket)
            for cur in clients_to_send:
                if cur in wlist:
                    cur.send(data.encode())
                    clients_to_send.remove(cur)
            messages_to_send.remove(message)

