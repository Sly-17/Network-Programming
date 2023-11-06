import socket
import sys

BUFFER_SIZE = 1024*10
PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 3440

server_address = ("localhost", PORT)

def make_request(resource):

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(server_address)
    print(f'Making HTTP request for resource {resource}');
    request_header = f'GET http://mysite.com/{resource} HTTP/1.0\nConnection : close\n'
    request_body = '\n'

    request = f'{request_header}\n{request_body}'

    client_socket.send(request.encode())

    response = client_socket.recv(BUFFER_SIZE).decode()
    client_socket.close();

    print(response + '\n\n')
    return response.split('\n\n')





request_obj = str(input('Enter Object to be requested : '))



response_header, response_body = make_request(request_obj)

data = response_body.split('\n')

for line in data:
    if line[:5] == "OBJ::":
        make_request(line[5:])
        




