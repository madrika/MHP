import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("127.0.0.1",4444))
s.listen(5)
print("connected")

c,addr = s.accept()

detail = c.recv(102456)
print(detail)


c.close()
