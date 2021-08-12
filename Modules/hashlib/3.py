import hashlib

data = [b'MHP123' , b'MHP456' , b'MHP789']

for d in data:
    print(hashlib.sha256(d).hexdigest())
