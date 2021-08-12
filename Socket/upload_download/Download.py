from socket import *

s = socket(2,1)
s.connect(("127.0.0.1",4444))
print("connected")

while True:
     name  = (s.recv(1024)).decode()
     file = open("new_"+name,"wb")
     data = (s.recv(1024)).decode()
     s.send("Yes !".encode())
     my_write = (s.recv(int(data)))
     file.write(my_write)
     file.close()

s.close()
