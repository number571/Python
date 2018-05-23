keys = {
'B':'Z','C':'X','D':'W','F':'V','G':'T',
'H':'S','J':'R','K':'Q','L':'P','M':'N'}
message = list(input("Write the text: ").upper())
for symbol in range(len(message)):
	for key in keys:
		if message[symbol] == key:
			message[symbol] = keys[key]
		elif message[symbol] == keys[key]:
			message[symbol] = key
		else: pass
print("Final message:","".join(message))