from socket import *

s = socket(AF_INET, SOCK_DGRAM) #UDP Connection

s.sendto("Hi ".encode() , ("127.0.0.1",1234))

while True:
    data = s.recv(1024)
    print("recv=> " +data.decode())
    msg = input("You> ")
    s.sendto(msg.encode(),("127.0.0.1",1234))

s.close()
