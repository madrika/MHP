from socket import *

s=socket(2,1)

s.bind(("127.0.0.1",1234))
s.listen(5)

c,addr=s.accept()

f=open("new.txt","w")
data=c.recv(1024)
f.write(data.decode())
f.close()
s.close()
