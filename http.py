import socket
import os

server_socket = socket.socket()
server_socket.bind(("127.0.0.1", 80))
server_socket.listen()
is_closed = False


def get_file(request):
    file = open(request, "rb")
    file_name = os.path.splitext(request)
    file_extension = file_name[1]
    file_extension = file_extension.removeprefix(".")
    file_contents = file.read()
    body = file_contents
    if file_extension == "jpg" or file_extension == "png":
        file_type = "image"
    else:
        file_type = "text"
    header = 'HTTP/1.1 200 OK\r\nContent-Length: ' + str(len(file_contents)) + '\r\n' + 'Content-Type: ' + \
             file_type + "/" + file_extension + '\r\n\r\n'
    response = header.encode() + body
    return response


def calc_next(request):
    if request[1].find('?') != -1:
        param = request[1].split('?')[1]
        print("test")
        param = param.split("=")[1]
        param = int(param)
        body = param + 1
        body = str(body)
        header = 'HTTP/1.1 200 OK \r\nContent-Length: ' + str(len(body)) + '\r\n\r\n'
        response = header.encode() + body.encode()
    else:
        return not_found()
    return response


def calc_area(request):
    if request[1].find('?') != -1:
        params = request[1].split('?')
        param1, param2 = params[1].split('&')
        param1 = param1.split("=")[1]
        param2 = param2.split("=")[1]
        body = (int(param1)*int(param2))/2
        body = str(body)
        header = 'HTTP/1.1 200 OK \r\nContent-Length: ' + str(len(body)) + '\r\n\r\n'
        response = header.encode() + body.encode()
    else:
        return not_found()
    return response


def not_found():
    file_contents = b"nope"
    header = 'HTTP/1.1 404 Not Found\r\nContent-Length: ' + str(len(file_contents)) + '\r\n\r\n'
    response = header.encode() + file_contents
    return response


def run_server():
    while not is_closed:
        (client_socket, client_address) = server_socket.accept()
        print("Connected")
        try:
            request_text = ''
            while request_text[len(request_text) - 4:] != '\r\n\r\n':
                request_text += client_socket.recv(1).decode()

            lines = request_text.split("\r\n")
            raw_request = lines[0].split(" ", 2)
            if raw_request[0] == "GET" and raw_request[2] == "HTTP/1.1":
                request_body = raw_request[1].lstrip("/\\").split('?')[0]
                print(request_body)
                print(raw_request)
                default_response = b''

                if request_body[0:14] == "calculate-next":
                    default_response = calc_next(raw_request)

                elif request_body[0:14] == "calculate-area":
                    default_response = calc_area(raw_request)

                elif os.path.isfile(request_body):
                    default_response = get_file(request_body)

                else:
                    default_response = not_found()
                print(default_response)
                client_socket.send(default_response)
                client_socket.close()

        except ConnectionResetError:
            pass


run_server()
