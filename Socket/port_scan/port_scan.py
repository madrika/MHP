import socket

while True:
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    ip= input("ip= ")
    port= input("port= ")

    try:
        s.connect((ip,int(port)))

        print("open port")
        print()
        print("_______________________")

    except:

        print("close port")
        print()
        print("_______________________")
