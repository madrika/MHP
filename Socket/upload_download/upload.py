from socket import *

s = socket(2,1)
s.bind(("127.0.0.1",4444))
s.listen(5)
print("connected")

c,addr = s.accept()

while True:
     name = input("Enter Your File Name : ")
     c.sendall(name.encode())
     f = open(name,"rb")
     data = memoryview(f.read())
     c.sendall(str(len(data)).encode())
     print(c.recv(1024))
     c.sendall(data)
     f.close()

c.close()
s.close()
     

     
