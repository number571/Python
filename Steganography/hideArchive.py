#!/usr/bin/python3

from sys import argv

# chmod +x main.py
# ./main.py file.jpg archive.zip

try:
	nameFile, archiveFile = argv[1], argv[2]
except IndexError:
	print("Error: Arguments!")
	raise SystemExit

try: 
	with open(nameFile, 'rb') as file: 
		readFile = file.read() 
	with open(archiveFile, 'rb') as archive:
		readArchive = archive.read() 
except FileNotFoundError: 
	print("Error: File is not found!")
	raise SystemExit 

with open(nameFile, 'wb') as file3:
	file3.write(readFile) 
	file3.write(readArchive) 
	print("[+] File: successfully overwritten!") 
