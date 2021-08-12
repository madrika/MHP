from socket import *
import pyautogui

s = socket(2,1)
s.connect(("127.0.0.1",4444))
print("connected")

screenshot = pyautogui.screenshot()
screenshot.save("screen.png")

f = open("screen.png","rb")
data = memoryview(f.read())
s.send(str(len(data)).encode())
print(s.recv(1024))
s.send(data)
f.close()

s.close()
