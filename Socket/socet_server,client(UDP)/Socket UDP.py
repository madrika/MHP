#UDP
from socket import *

s=socket(AF_INET, SOCK_DGRAM) #UDP connection

s.bind(("127.0.0.1",1212))

print("server Running on port 1212")

c , addr = s.recvfrom(1024)

print("connected to"+str(addr)+"\n")

print("Recived = "+str(c))

s.sendto("Heloo I am server".encode(),addr)

s.close()
