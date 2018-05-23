from re import findall
keysPolibiy = {
	'A':'11', 'B':'12', 'C':'13', 'D':'14',
	'E':'15', 'F':'16', 'G':'21', 'H':'22',
	'I':'23', 'J':'24', 'K':'25', 'L':'26',
	'M':'31', 'N':'32', 'O':'33', 'P':'34',
	'Q':'35', 'R':'36', 'S':'41', 'T':'42',
	'U':'43', 'V':'44', 'W':'45', 'X':'46',
	'Y':'51', 'Z':'52', '0':'53', '1':'54',
	'2':'55', '3':'56', '4':'61', '5':'62',
	'6':'63', '7':'64', '8':'65', '9':'66'
}
cryptMode = input("[E]ncrypt|[D]ecrypt: ").upper()
if cryptMode not in ['E','D']:
	print("Error: mode is not Found!"); raise SystemExit
startMessage = input("Write the message: ").upper()
def regular(text):
	template = r"[0-9]{2}"
	return findall(template, text)
def encryptDecrypt(mode, message, final = []):
	if mode == 'E':
		for symbol in message:
			if symbol in keysPolibiy:
				final.append(keysPolibiy[symbol]) 
	else:
		for twoNumbers in regular(message):
			for key in keysPolibiy:
				if twoNumbers == keysPolibiy[key]:
					final.append(key)
	return ".".join(final)
print("Final message:",encryptDecrypt(cryptMode, startMessage))