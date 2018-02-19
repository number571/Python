cryptMode = input("[E]ncrypt|[D]ecrypt: ").upper()
if cryptMode not in ['E','D']:
	print("Error: mode is not Found!"); raise SystemExit
startMessage = input("Write the message: ").upper()
oneKey = input("Write the key: ").upper()
def encryptDecrypt(mode, message, key, final = ""):
	key *= len(message) // len(key) + 1
	for index, symbol in enumerate(message):
		if mode == 'E':
			temp = ord(symbol) + ord(key[index])
		else:
			temp = ord(symbol) - ord(key[index])
		final += chr(temp % 26 + ord('A'))
	return final
print("Final message:",encryptDecrypt(cryptMode, startMessage, oneKey))