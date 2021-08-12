import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect(('192.168.1.1',80))

print("connected")

s.send("GET /index.php HTTP/1.0 \n\n".encode())

data = s.recv(1234)

print(data.decode())

s.close()

