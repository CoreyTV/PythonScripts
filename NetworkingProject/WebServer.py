# import socket module
from socket import *
import sys  # In order to terminate the program

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('127.0.0.1', 80))
serverSocket.listen(1)
while True:

    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()

    try:
        message = connectionSocket.recv(4096)
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata =  f.read();
        data= ' HTTP/1.1 200 OK\nConnection: Close\nContent-Type: text/html\nContent-Length: %d\n\n' % (len(outputdata))
        connectionSocket.send(data.encode())
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
    except IOError:
        data = ' HTTP/1.1 404 Not Found\n\n'
        connectionSocket.send(data.encode())
        connectionSocket.send("<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n".encode())
  # Terminate the program after sending the corresponding data
