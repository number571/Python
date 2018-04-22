from pyAesCrypt import encryptFile, decryptFile
from os import remove
from os.path import splitext
cryptMode = input("[E]ncrypt|[D]ecrypt: ").upper()
if cryptMode not in ['E','D']:
	print("Error: mode is not Found!"); raise SystemExit
fileName = input("Write the file: ")
paswFile = input("Write the password: ")
bufferSize = 64*1024
def encryptDecrypt(mode, file, password, final = ""):
	if mode == 'E':
		try: 
			encryptFile(str(file), str(file)+".crp", password, bufferSize)
			remove(file)
		except FileNotFoundError: return "[x] File not found!"
		else: return "[+] File '{name}' overwritten!".format(name = str(file))
	else:
		try: 
			decryptFile(str(file), str(splitext(file)[0]), password, bufferSize)
			remove(file)
		except FileNotFoundError: return "[x] File not found!"
		except ValueError: return "[x] Password is False!"
		else: return "[+] File '{name}' overwritten!".format(name = str(file))
print(encryptDecrypt(cryptMode, fileName, paswFile))
