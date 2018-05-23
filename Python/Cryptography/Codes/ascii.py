codeMode = input("[E]ncode|[D]ecode: ").upper()
if codeMode not in ['E','D']:
	print("Error: mode is not Found!"); raise SystemExit
startMessage = input("Write the message: ")
def encodeDecode(mode, message, final = ""):
	if mode == 'E':
		for symbol in message:
			final += str(ord(symbol)) + ' '
	else:
		for code in message.split():
			final += chr(int(code))
	return final
print("Final message:",encodeDecode(codeMode, startMessage))
