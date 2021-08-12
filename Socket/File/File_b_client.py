from socket import *

s = socket(2,1)
s.connect(("127.0.0.1",4444))
print("connected")

while True:
     name = s.recv(1024)
     f = open(name.decode(),"rb")
     data = memoryview(f.read())
     s.send(str(len(data)).encode())
     print(s.recv(1024).decode())
     s.send(data)
     f.close()

s.close()
