from random import randint
from re import findall
cryptMode = input("[E]ncrypt|[D]ecrypt: ").upper()
if cryptMode not in ['E','D']:
	print("Error: mode is not Found!"); raise SystemExit
startMessage = input("Write the message: ").upper()
def regular(text):
	template = r"[0-9]+"
	return findall(template, text)
def encryptDecrypt(mode, message, final = "", keys = []):
	if mode == 'E':
		for symbol in message:
			key = randint(0,25); keys.append(str(key))
			final += chr((ord(symbol) + key - 13)%26 + ord('A'))
		return final, '.'.join(keys)
	else: 
		keys = input("Write the keys: ")
		for index, symbol in enumerate(message):
			final += chr((ord(symbol) - int(regular(keys)[index]) - 13)%26 + ord('A'))
		return final
print("Final message:",encryptDecrypt(cryptMode, startMessage))