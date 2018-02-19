from re import findall
keysPsevdo = {
	'A':"AAA", 'B':"AAА", 'C':"AAΑ",
	'D':"AАA", 'E':"AАА", 'F':"AАΑ",
	'G':"AΑA", 'H':"AΑА", 'I':"AΑΑ",
	'J':"АAA", 'K':"АAА", 'L':"АAΑ",
	'M':"ААA", 'N':"ААА", 'O':"ААΑ",
	'P':"АΑA", 'Q':"АΑА", 'R':"АΑΑ",
	'S':"ΑAA", 'T':"ΑAА", 'U':"ΑAΑ",
	'V':"ΑАA", 'W':"ΑАА", 'X':"ΑАΑ",
	'Y':"ΑΑA", 'Z':"ΑΑА", ' ':"ΑΑΑ"
}
cryptMode = input("[E]ncrypt|[D]ecrypt: ").upper()
if cryptMode not in ['E','D']:
	print("Error: mode is not Found!"); raise SystemExit
startMessage = input("Write the message: ").upper()
def regular(text):
	template = r"\w{3}"
	return findall(template, text)
def encryptDecrypt(mode, message, final = ""):
	if mode == 'E':
		for symbol in message:
			if symbol in keysPsevdo:
				final += keysPsevdo[symbol]
	else:
		for threeSymbols in regular(message):
			for key in keysPsevdo:
				if threeSymbols == keysPsevdo[key]:
					final += key
	return final
print("Final message:",encryptDecrypt(cryptMode, startMessage))