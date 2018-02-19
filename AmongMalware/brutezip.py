#!/usr/bin/python3

from zipfile import ZipFile
from sys import argv
from os import mkdir

# chmod +x main.py
# ./main.py archive.zip rockyou.txt

try:
	archiveFile, dictionaryFile = argv[1], argv[2]
except IndexError:
	print("Error: Arguments!")
	raise SystemExit

line = "----------------------------------"
def generator(string):
	for word in string:
		passwd = word.replace('\n','')
		archive.setpassword(passwd.encode())
		try: 
			archive.extractall(directory)
		except: 
			yield "[False]: " + passwd
		else: 
			yield line + "\n[True]: " + passwd; return

directory = "ExtractArchive"
try: mkdir(directory)
except FileExistsError: pass

print(line)
with open(dictionaryFile, errors='ignore') as dictionary:
	with ZipFile(archiveFile) as archive:
		print(line)
		for password in generator(dictionary):
			print(password)
print(line)