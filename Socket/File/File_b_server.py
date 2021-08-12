from socket import *

s = socket(2,1)
s.bind(("127.0.0.1", 4444))
s.listen(5)


c,addr = s.accept()
print("connected")

while True:
     name = input("Enter Your File Name : ")
     c.sendall(name.encode())
     f = open("new_"+name,"wb")
     data = c.recv(1024)
     c.sendall("Recived Data Len".encode())
     my_write = (c.recv(int(data.decode())))
     f.write(my_write)
     f.close()

s.close()
