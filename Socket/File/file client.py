from socket import *

s=socket(2,1)
s.connect(("127.0.0.1",1234))
f=open("test.txt","r")
data=f.read()
s.send(data.encode())
f.close()
s.close()
