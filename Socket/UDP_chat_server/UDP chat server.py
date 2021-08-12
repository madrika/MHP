from socket import *

s = socket(AF_INET,SOCK_DGRAM) #UDP Connection

s.bind(("127.0.0.1",1234))

print("\nUDP Chat Server Running on Port 1234\n")

c , addr = s.recvfrom(1024)

while True:
        msg = input("You=> ")
        s.sendto(msg.encode(),addr)
        data = s.recv(1024)
        print("recv => "+data.decode())
        
s.close()
