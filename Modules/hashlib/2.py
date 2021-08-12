import hashlib

a=hashlib.md5()

a.update(b'python')

print(a.digest())
