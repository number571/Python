#!/usr/bin/python3

from sys import argv

# chmod +x main.py
# ./main.py file.jpg

try:
	nameFile = argv[1]
	textFile = argv[2:]
except IndexError:
	print("Error: Arguments!"); raise SystemExit
	
with open(nameFile, 'ab') as file: 
	file.write("".join(textFile).encode("utf-8")) 
	print("[+] File successfully overwritten!")
