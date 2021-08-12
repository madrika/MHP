from socket import *
import pyaes

key = "key_is_python_AH".encode()

aes = pyaes.AESModeOfOperationCTR(key)

s = socket(2,1)
s.connect(("127.0.0.1",4444))

print(aes.decrypt(s.recv(1024)))

s.close()
