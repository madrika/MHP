import telnetlib
import time

IP = "192.168.10.100"
USERNAME = "Madrika"
PASSWORD = "Madrika"
ENABLE_PASS = "Madrika"

telnet = telnetlib.Telnet(IP)
telnet.read_until("Username: ".encode())
time.sleep(3)
telnet.write(USERNAME.encode() + "\n".encode())
time.sleep(3)
telnet.read_until("Password: ".encode())
telnet.write(PASSWORD.encode() + "\n".encode())
time.sleep(1)
telnet.write("en\n".encode())
time.sleep(1)
telnet.write(ENABLE_PASS.encode() + "\n".encode())
time.sleep(1)
telnet.write("conf t\n".encode())
time.sleep(1)
telnet.write("hostname Madrika\n".encode())
time.sleep(1)
telnet.write("end\n".encode())
time.sleep(1)
telnet.write("exit\n".encode())


