import socket
from datetime import*

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind(("127.0.0.1", 1212))
s.listen(5)

while True:
    client , addr = s.accept()
    print("connected to "+str(addr)+"\n")
    today=date.today()
    client.sendall("today's date:".encode()+str(today).encode())

client.close()
