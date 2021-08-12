import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect(("127.0.0.1", 2323))

print("connected \n")

data=s.recv(1024)

print(data.decode())

s.send("Hello I am client".encode())

s.close()
