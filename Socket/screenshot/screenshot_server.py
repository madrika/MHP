from socket import *

s = socket(2,1)
s.bind(("127.0.0.1",4444))
s.listen(5)
print("connected")

c,addr = s.accept()

f = open("screen.png", "wb")
data = c.recv(1024)
c.send("Recv data !".encode())
data_all = (c.recv(int(data)))
f.write(data_all)
f.close()


c.close()
s.close()
            
