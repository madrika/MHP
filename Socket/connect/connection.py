import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #tcp connection

s.connect(('127.0.0.1',80))

print('connected')

s.close()
