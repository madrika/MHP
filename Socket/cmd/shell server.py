from socket import *

s=socket(AF_INET,SOCK_STREAM)
s.bind(("127.0.0.1",4444))
s.listen(5)
print("shell server running on port 4444\n")
c , addr = s.accept()
print("connected to "+str(addr)+"\n")

while True:
    cmd = input("shell=> ")
    c.sendall(cmd.encode())
    cmd_output = c.recv(12345)
    print(cmd_output.decode())
    print()

c.close()
