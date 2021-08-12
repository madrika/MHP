import paramiko
import time

IP = "192.168.20.1"
USERNAME = "Madrika"
PASSWORD = "Madrika"
ENABLE_PASS = "Madrika"

SSH = paramiko.SSHClient()
SSH.set_missing_host_key_policy(paramiko.AutoAddPolicy())
SSH.connect(IP, username=USERNAME, password=PASSWORD)
Console = SSH.invoke_shell()
Console.recv(65535)
Console.send("en\n".encode())
time.sleep(1)
Console.send(ENABLE_PASS.encode() + "\n".encode())
time.sleep(1)
Console.send("conf t\n".encode())
time.sleep(1)
Console.send("hostname Madrika\n".encode())
time.sleep(1)
Console.recv(65535)
Console.send("end\n".encode())
time.sleep(1)
SSH.close()

