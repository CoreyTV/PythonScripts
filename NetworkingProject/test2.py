from socket import *
import sys


# Create a server socket, bind it to a port and start listening
tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(('', 8888))
tcpSerSock.listen(100)

while 1:
    # Strat receiving data from the client
    print('Ready to serve...')
    tcpCliSock, addr = tcpSerSock.accept()
    print('Received a connection from:', addr)
    message = tcpCliSock.recv(1024).decode()
    print(message)
    # Extract the filename from the given message
    print(message.split()[1])
    filename = message.split()[1].partition("/")[2]
    print(filename)
    fileExist = "false"
    filetouse = "/" + filename
    print(filetouse)
    try:
        # Check wether the file exist in the cache
        f = open(filetouse[1:], "r")
        outputdata = f.readlines()
        fileExist = "true"
        # ProxyServer finds a cache hit and generates a response message
        tcpCliSock.send("HTTP/1.0 200 OK\r\n")
        tcpCliSock.send("Content-Type:text/html\r\n")
        for i in range(0, len(outputdata)):
            tcpCliSock.send(outputdata[i])
            print('Read from cache')
        # Error handling for file not found in cache
    except IOError:
        if fileExist == "false":
            # Create a socket on the proxyserver
            c = socket(AF_INET, SOCK_STREAM)
            hostn = filename.replace("www.", "", 1)
            print(hostn)
            try:
                c.connect((hostn, 80))
                c.send(("GET " + "/" + " HTTP/1.0\r\n\r\n"))
                while 1:
                    reply= c.recv(1000000000)
                    if len(reply) > 0:
                        tcpCliSock.send(reply)
                        dar=float(len(reply))
                        dar=float(dar/1024)
                        dar="{}.3s".format(dar)

                    c.close()
                    tcpCliSock.close()


            except:
                print("Illegal request")
        else:
            # HTTP response message for file not found
            tcpCliSock.send("HTTP/1.0 404 sendErrorErrorError\r\n")
            tcpCliSock.send("Content-Type:text/html\r\n")
            tcpCliSock.send("\r\n")
    # Close the client and the server sockets
    tcpCliSock.close()
tcpSerSock.close()