from re import findall
cryptMode = input("[E]ncrypt|[D]ecrypt: ").upper()
if cryptMode not in ['E','D']:
	print("Error: mode is not Found!"); raise SystemExit
startMessage = input("Write the message: ")
def regular(text):
	return findall(r"[0-9]+", text)
def encryptDecrypt(mode, message, final = "", key = ""):
	if mode == 'E':
		for x in message: key += x if x not in key else ""
		encrypt = {key[x]:str(x) for x in range(len(key))}
		for symbol in message:
			final += encrypt[symbol] + ' '
		return (key, final)
	else:
		key = input("Write the key: ")
		for num in regular(message):
			final += key[int(num)]
		return final
print("Final message: ", encryptDecrypt(cryptMode, startMessage))
