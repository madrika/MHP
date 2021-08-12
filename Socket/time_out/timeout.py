from socket import *
import time

s = socket(AF_INET,SOCK_STREAM)
s.bind(("127.0.0.1",4444))
s.listen(5)

s.settimeout(6)
print("server connected")

try:
     client, addr = s.accept()
     print("connected to "+str(addr)+"\n")

except:
     print("server closed")

s.close()
