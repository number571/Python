codeMode = input("[E]ncode|[D]ecode: ").upper()
if codeMode not in ['E','D']:
	print("Error: mode is not Found!"); raise SystemExit
startMessage = input("Write the message: ").upper()
codes = {
	'A':'.-',	'N':'-.',	'1':'.----',	
	'B':'-...',	'O':'---',	'2':'..---',
	'C':'-.-.',	'P':'.--.',	'3':'...--',
	'D':'-..',	'Q':'--.-',	'4':'....-',
	'E':'.',	'R':'.-.',	'5':'.....',
	'F':'..-.',	'S':'...',	'6':'-....',
	'G':'--.',	'T':'-',	'7':'--...',
	'H':'....',	'U':'..-',	'8':'---..',
	'I':'..',	'V':'...-',	'9':'----.',
	'J':'.---',	'W':'.--',	'0':'-----',
	'K':'-.-',	'X':'-..-',
	'L':'.-..',	'Y':'-.--',
	'M':'--',	'Z':'--..',
}
def encodeDecode(mode, message, final = ""):
	if mode == 'E':
		for symbol in message:
			if symbol not in codes:
				message = message.replace(symbol, '')
		for symbol in message:
			final += codes[symbol] + ' '
	else:
		message = message.split(' ')
		for code in message:
			for symbol in codes:
				if code == codes[symbol]:
					final += symbol
	return final
print("Final message:",encodeDecode(codeMode, startMessage))
