cryptMode = input("[E]ncrypt|[D]ecrypt: ").upper()
if cryptMode not in ['E','D']:
	print("Error: mode is not Found!"); raise SystemExit

startMessage = input("Write the message: ").upper()
keyNumber = input("Write the keyNumber: ")

def encryptDecrypt(mode, message, key, final = ""):
	key *= len(message) // len(key) + 1
	for index, symbol in enumerate(message):
		if mode == 'E':
			temp = ord(symbol) + int(key[index]) -13
		else:
			temp = ord(symbol) - int(key[index]) -13
		final += chr(temp%26 + ord('A'))
	return final
print("Final message:",encryptDecrypt(cryptMode, startMessage, keyNumber))