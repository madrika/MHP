from socket import *
import pyaes

key = "key_is_python_AH".encode()

aes = pyaes.AESModeOfOperationCTR(key)

plain_text = "this is golden"
cipher_text = aes.encrypt(plain_text)
print(cipher_text)

s = socket(2,1)
s.bind(("127.0.0.1",4444))
s.listen(5)

while True:
     c,addr = s.accept()
     c.send(cipher_text)


c.close()
