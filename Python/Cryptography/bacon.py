from re import findall
keysBacon = {
	'A':"AAAAA", 'B':"AAAAB", 'C':"AAABA",
	'D':"AAABB", 'E':"AABAA", 'F':"AABAB",
	'G':"AABBA", 'H':"AABBB", 'I':"ABAAA",
	'J':"ABAAB", 'K':"ABABA", 'L':"ABABB",
	'M':"ABBAA", 'N':"ABBAB", 'O':"ABBBA",
	'P':"ABBBB", 'Q':"BAAAA", 'R':"BAAAB",
	'S':"BAABA", 'T':"BAABB", 'U':"BABAA",
	'V':"BABAB", 'W':"BABBA", 'X':"BABBB",
	'Y':"BBAAA", 'Z':"BBAAB", ' ':"BBABA"
}
cryptMode = input("[E]ncrypt|[D]ecrypt: ").upper()
if cryptMode not in ['E','D']:
	print("Error: mode is not Found!"); raise SystemExit
startMessage = input("Write the message: ").upper()
def regular(text):
	template = r"[A-Z]{5}"
	return findall(template, text)
def encryptDecrypt(mode, message, final = ""):
	if mode == 'E':
		for symbol in message:
			if symbol in keysBacon: final += keysBacon[symbol]
	else:
		for symbolsFive in regular(message):
			for key in keysBacon:
				if symbolsFive == keysBacon[key]: final += key
	return final
print("Final message:",encryptDecrypt(cryptMode, startMessage))