import hashlib

print("""
[+]-1 md5
[+]-2 sha1
[+]-3 sha224
[+]-4 sha256
[+]-5 sha384
[+]-6 sha512
""")

inputer = input("Enter Your password for hashling : ")
model = input("select the number options : ")

if model == "1":
	md5 = hashlib.md5()
	md5.update(inputer.encode())
	print("[*] md5 your password is > ",md5.hexdigest())
elif model == "2":
	sha1 = hashlib.sha1()
	sha1.update(inputer.encode())
	print("[*] sha1 your password is > ",sha1.hexdigest())
elif model == "3":
	sha224 = hashlib.sha224()
	sha224.update(inputer.encode())
	print("[*] sha224 your password is > ",sha224.hexdigest())
elif model == "4":
	sha256 = hashlib.sha256()
	sha256.update(inputer.encode())
	print("[*] sha256 your password is > ",sha256.hexdigest())
elif model == "5":
	sha384 = hashlib.sha384()
	sha384.update(inputer.encode())
	print("[*] sha384 your password is > ",sha384.hexdigest())
elif model == "6":
	sha512 = hashlib.sha512()
	sha512.update(inputer.encode())
	print("[*] sha512 your password is > ",sha512.hexdigest())
else:
	exit()
