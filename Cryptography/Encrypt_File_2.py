from cryptography.fernet import Fernet

key = Fernet.generate_key()

print(key)

file = open("1.jpg","rb")

data = file.read()

file.close()

#print data

New_File = open("1enc.jpg","wb")

f = Fernet(key)

Encrypt = f.encrypt(data)

New_File.write(Encrypt)

New_File.close()


#key = vsgDfJ8ZDKP8vT2dMXnRNyzcKvBasBhgO9pF7HQvAiA=
