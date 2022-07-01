from socket import *

c = socket(AF_INET, SOCK_STREAM)

hostn = 'google.com'

print (hostn)


c.connect((hostn,80))

print('Socket connected to port 80 of the host')


fileobj = c.makefile('rwb')

string1 = "GET " + "/images/nav_logo229.png" + " HTTP/1.0\n\n"

naming = bytes(string1,'utf-8')

c.send(naming)

fileobj.write(naming)

buff = fileobj.readlines()
print(buff)
c.close()