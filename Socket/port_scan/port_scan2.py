import socket

while True:
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    ip = input("ip= ")
    port = input("port= ")
    r = s.connect_ex((ip,int(port)))

    if r==0:
        print("open port")
    else:
        print("close port")

s.close()
