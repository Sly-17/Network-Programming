import socket                                                                                                                                              
import sys                                                                                                                                                 
import datetime                                                                                                                                            
import threading                                                                                                                                           
                                                                                                                                                           
                                                                                                                                                           
PORT = int(sys.argv[1])                                                                                                                                    
BUFFER_SIZE = 1024 * 10                                                                                                                                    
                                                                                                                                                           
def handle_request(req):                                                                                                                                   
    print(req + '\n\n')                                                                                                                                    
    req_header, req_body = req.split('\n\n')                                                                                                               
    method, url, version = req_header.split('\n')[0].split(' ')                                                                                            
                                                                                                                                                           
    try:                                                                                                                                                   
        f = open(f"./data/{url.split('/')[3]}", "r")                                                                                                       
        response_body = f.read()                                                                                                                           
        response_header = f'{version} 200 OK\nDate : {datetime.datetime.now()}\nContent-Length : {len(response_body)}\n'                                   
                                                                                                                                                           
    except FileNotFoundError:                                                                                                                              
        response_header = f'{version} 404 NOT FOUND\nConnection : close\n'                                                                                 
        respose_body = ''                                                                                                                                  
                                                                                                                                                           
    response = f'{response_header}\n{response_body}'                                                                                                       
    return response                                                                                                                                        
                                                                                                                                                           
                                                                                                                                                           
def handle_client(client_socket):                                                                                                                          
    while(True):                                                                                                                                           
        request = client_socket.recv(BUFFER_SIZE).decode();                                                                                                
        response = handle_request(request)                                                                                                                 
                                                                                                                                                           
        client_socket.send(response.encode())                                                                                                              
                                                                                                                                                           
    client_socket.close()                                                                                                                                  
                                                                                                                                                           
                                                                                                                                                           
server_address = ("localhost", PORT)                                                                                                                       
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)                                                                                          
                                                                                                                                                           
server_socket.bind(server_address)                                                                                                                         
server_socket.listen(10)                                                                                                                                   
                                                                                                                                                           
threads = []                                                                                                                                               
                                                                                                                                                           
while(True):                                                                                                                                               
    client_socket, client_address = server_socket.accept()                                                                                                 

    thread = threading.Thread(target = handle_client, args = (client_socket,))                                                                             
    threads.append(thread)                                                                                                                                 
    thread.setDaemon(True)                                                                                                                                 
    thread.start()                                                                                                                                         
                                                                                                                                                           
                                                                                                                                                           
for thread in threads:                                                                                                                                     
    thread.join()                                                                                                                                          
                        
