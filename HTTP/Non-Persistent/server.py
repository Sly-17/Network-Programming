import socket
import datetime
import sys


PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 3440
BUFFER_SIZE = 1024 * 4
newline = '\n'

def handle_HTTP_request(req):
    # Request message format -> METHOD URL VERSION

    req_headers, req_body = req.split('\n\n')
    print(f'REQUEST HEADERS : \n{req_headers}')
    print(f'REQUEST BODY : \n{req_body}')


    method, resource, version = req_headers.split('\n')[0].split(' ')
    print(resource.split('/')[3])


    try:
        f = open(f"./data/{resource.split('/')[3]}", "r")
        response_body = f.read();
        f.close();

        response_header = newline.join([f'{version} 200 OK',
                                        f'Connection : close',
                                        f'Date : {datetime.datetime.now()}',
                                        f'Content-Length : {len(response_body)}'])

        response = newline.join([f'{response_header}\n', f'{response_body}'])

    except FileNotFoundError:
        response_header = newline.join([f'{version} 404 NOT FOUND', f'Connection : close'])
        response = response_header + '\n'

    return response;



server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ("localhost", PORT);
server_socket.bind(server_address)

server_socket.listen(5)
print(f"HTTP SERVER LISTENING AT PORT {PORT}");


while True:
    (client_socket, client_address) = server_socket.accept()

    request = client_socket.recv(BUFFER_SIZE).decode()

    response = handle_HTTP_request(request);


    client_socket.send(response.encode())

    client_socket.close()
