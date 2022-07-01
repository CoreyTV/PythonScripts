import socket
import time
destination= ('localhost',12000)
clientSocket=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
clientSocket.settimeout(1)  # waiting the 1 second for a reply or assuming it is lost
for i in range(1,11):
    time1=time.time()
    ping = ("Ping %d %s" % (i, time1)).encode()
    try:
        clientSocket.sendto(ping, destination)
        pong, ipAddr = clientSocket.recvfrom(1024)
        time2= time.time()-time1
        print("Pong: %d Reply from %s Round Trip Time = %.6fs" % (i, ipAddr, time2))
    except socket.timeout:
        print("Ping %d Timed Out" % (i))
clientSocket.close()