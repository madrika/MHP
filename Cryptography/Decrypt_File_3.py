from cryptography.fernet import Fernet

key = "vsgDfJ8ZDKP8vT2dMXnRNyzcKvBasBhgO9pF7HQvAiA="


file = open("1enc.jpg","rb")

data = file.read()

file.close()

#print data

New_File = open("1.jpg","wb")

f = Fernet(key)

Decrypt = f.decrypt(data)

New_File.write(Decrypt)

New_File.close()



