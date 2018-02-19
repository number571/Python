cryptMode = input("[E]ncrypt|[D]ecrypt: ").upper()
if cryptMode not in ['E','D']:
	print("Error: mode is not Found!"); raise SystemExit

startMessage = list(input("Write the message: ").upper())
for symbol in startMessage:
	if symbol not in [chr(x) for x in range(65,91)]:
		startMessage.remove(symbol)
funcKey = lambda x: x*2

def encryptDecrypt(mode, message, key, final = ""):
	for index, symbol in enumerate(message):
		if mode == 'E':
			temp = ord(symbol) + key(index) - 13
		else:
			temp = ord(symbol) - key(index) - 13
		final += chr(temp%26 + ord('A'))
	return final
print("Final message:",encryptDecrypt(cryptMode, startMessage, funcKey))