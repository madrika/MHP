import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(("127.0.0.1", 2323))
s.listen(5)
print("connected on port 2323\n")
client , addr =s.accept()
print("connected to " + str(addr)+"\n")
client.sendall("Heloo I am server".encode())
data = client.recv(1024)
print(data.decode())
client.close()
