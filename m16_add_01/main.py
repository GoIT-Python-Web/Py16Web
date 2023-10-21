
import hashlib

names = {"Nata": 16, "Bogdan": 24, "Nastya": 20}

print(hash("Nata"))
print(hash("Bogdan"))
print(hash("Nastya"))

hashed_nata = hashlib.md5('Nata'.encode())
print(hashed_nata.digest())
print(hashed_nata.hexdigest())