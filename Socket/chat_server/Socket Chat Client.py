import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

ip=input("Enter ip : ")
port=input("Enter port : ")
name=input("Enter name : ")

s.connect((ip,int(port)))

print("connected to server "+str(port)+("\n"))

while True:
    data=s.recv(1024)
    print(data.decode())
    msg=input("-> ")
    s.send(name.encode()+"--> ".encode()+msg.encode())


s.close()
