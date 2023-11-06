import socket                                                                                                                                              
import threading                                                                                                                                           
import datetime                                                                                                                                            
import sys                                                                                                                                                 
                                                                                                                                                           
PORT = int(sys.argv[1])                                                                                                                                    
BUFFER_SIZE = 1024 * 10                                                                                                                                    
                                                                                                                                                           
def make_HTTP_request(client_socket, resource):                                                                                                            
    print(f'Making request for resource {resource}\n')                                                                                                     
    req_header = f'GET http://mysite.com/{resource} HTTP/1.1\nConnection : Keep-Alive\n'                                                                   
    req_body = ''                                                                                                                                          
    request = f'{req_header}\n{req_body}'                                                                                                                  
    client_socket.send(request.encode())                                                                                                                   

    response = client_socket.recv(BUFFER_SIZE).decode()                                                                                                    
    print(response)                                                                                                                                        
                                                                                                                                                           
    return response.split('\n\n')                                                                                                                          
                                                                                                                                                           
                                                                                                                                                           
                                                                                                                                                           
resource = str(input('Resource to be requested : '))                                                                                                       
                                                                                                                                                           
server_address = ("localhost", PORT)                                                                                                                       
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);                                                                                         
                                                                                                                                                           
client_socket.connect(server_address)                                                                                                                      
                                                                                                                                                           
response_header, response_body = make_HTTP_request(client_socket, resource)                                                                                
threads = []                                                                                                                                               
                                                                                                                                                           
for line in response_body.split('\n'):                                                                                                                     
    if(line[:5] == "OBJ::"):                                                                                                                               
        thread = threading.Thread(target = make_HTTP_request, args = (client_socket, line[5:]))                                                            
        threads.append(thread)                                                                                                                             
        thread.setDaemon(True)                                                                                                                             
        thread.start()                                                                                                                                     
                                                                                                                                                           
                                                                                                                                                           
for thread in threads:                                                                                                                                     
    thread.join()                                                                                                                                          
                                                                                                                                                           
client_socket.close();
