#!/usr/bin/python3

from sys import argv
from hashlib import sha256, sha512, md5

# chmod +x main.py
# ./main.py sha256 hash.txt rockyou.txt

line = "----------------------------------"

try:
	hashAlgr,fileHash,fileDict = argv[1],argv[2],argv[3]
except IndexError:
	print("Error: Arguments!")
	raise SystemExit

with open(fileHash) as file:
	hashFunc = file.read()
	hashFunc = hashFunc.replace('\n','')

def generator(string):
	for word in string:
		passwd = word.replace('\n','')
		if encrypt(passwd) == hashFunc:
			yield line +"\n[True]: "+passwd
			return
		else:
			yield "[False]: "+passwd

def encrypt(string):
	passwd = string.encode()
	if hashAlgr == "md5":
		signature = md5(passwd).hexdigest()
	elif hashAlgr == "sha256":
		signature = sha256(passwd).hexdigest()
	elif hashAlgr == "sha512":
		signature = sha512(passwd).hexdigest()
	else: raise SystemExit
	return signature

print(line)
with open(fileDict, errors = "ignore") as dictionary:
	for password in generator(dictionary):
		print(password)
print(line)