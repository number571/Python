cryptMode = input("[E]ncrypt|[D]ecrypt: ").upper()
if cryptMode not in ['E','D']:
	print("Error: mode is not Found!"); raise SystemExit
startMessage = input("Write the message: ")

def encryptDecrypt(mode, message, final = ""):
	if mode == 'E':
		encryptList = [
[message[x] for x in range(len(message)) if x%2 == 0],
[message[x] for x in range(len(message)) if x%2 != 0]
]
		for index in range(len(encryptList)):
			final += "".join(encryptList[index])
	else:
		if len(message)%2 != 0: message += " "
		length, half = len(message), len(message)//2
		decryptList = [
[message[x] for x in range(half)],
[message[x] for x in range(half,length)]
]
		for index in range(half):
			final += decryptList[0][index]+decryptList[1][index]
	return final
print("Final message:",encryptDecrypt(cryptMode, startMessage))