from cryptography.fernet import Fernet


key = "m8WrcrKNKa81MAz0XpPukZzK4Aawm18QTPT6XLYGlMs="

Encrypt = "gAAAAABfxmSz0bC7OG6jP3zBCzgnP6ypK_z1VbUj3hs9dQBvLHrkI3Lh_iLfUINli8evK8cJOXJf5MeX8R_AXdohY5ht_gNWZQ=="

f = Fernet(key)

Decrypt = f.decrypt(Encrypt)

print(Decrypt)
