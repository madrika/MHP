import paramiko
import time


#from  paramiko import SSHClient


IP = open("IP.txt")
USERNAME = "Madrika"
PASSWORD = "Madrika"
ENABLE_PASS = "Madrika"

for line in IP.readlines():
    HOST = line.strip()
    SSH = paramiko.SSHClient()
    SSH.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    SSH.connect(HOST, username=USERNAME, password=PASSWORD)
    Console = SSH.invoke_shell()
    Console.recv(65535)
    Console.send("en\n".encode())
    time.sleep(1)
    Console.send(ENABLE_PASS.encode() + "\n".encode())
    time.sleep(1)
    Console.send("conf t\n".encode())
    time.sleep(1)
    Console.send("hostname Pythonnetwork\n".encode())
    time.sleep(1)
    Console.recv(65535)
    Console.send("end\n".encode())
    time.sleep(1)
    SSH.close()
