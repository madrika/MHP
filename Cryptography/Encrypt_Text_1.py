import cryptography.fernet

key = cryptography.fernet.Fernet.generate_key()

print(key)

text = "Hello World"

f = cryptography.fernet.Fernet(key)

Encrypt = f.encrypt(text)

print(Encrypt)

#key = m8WrcrKNKa81MAz0XpPukZzK4Aawm18QTPT6XLYGlMs=
#encrypt = gAAAAABfxmSz0bC7OG6jP3zBCzgnP6ypK_z1VbUj3hs9dQBvLHrkI3Lh_iLfUINli8evK8cJOXJf5MeX8R_AXdohY5ht_gNWZQ==
