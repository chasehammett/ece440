#import socket module
from socket import *
# import socket
import sys # In order to terminate the program

serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a sever socket
#Fill in start
# dest = socket.gethostbyname(host)
port = 10132
serverSocket.bind((gethostname(), port))
serverSocket.listen(1)
# HOST, PORT = '', 8888

# serverSocket = serverSocket.socket(socket.AF_INET, socket.SOCK_STREAM)
# serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# serverSocket.bind((HOST, PORT))
# serverSocket.listen(1)
# Fill in end
while True:
    #Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()# serverSocket.accept()          
    try:
        connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n") # ok message
        message = connectionSocket.recv(1024)   #Fill in start          #Fill in end               
        filename = message.split()[1]                 
        f = open(filename[1:])                        
        outputdata = f.read() #Read html file Fill in start       #Fill in end                   
        #Send one HTTP header line into socket
        #Fill in start

        # http_response = """\
        # HTTP/1.1 200 OK

        # Hello, World!
        # """
        #Fill in end                
        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):           
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        
        connectionSocket.close()
    except IOError:
        #Send response message for file not found
        #Fill in start   
        connectionSocket.send("ERROR 404 : PAGE NOT FOUND")     
        #Fill in end
        #Close client socket
        #Fill in start
        connectionSocket.close()  
        #Fill in end            
serverSocket.close()
sys.exit()#Terminate the program after sending the corresponding data    