keys = {
	'A':'B','C':'D','E':'F','G':'H','I':'J','K':'L',
	'M':'N','O':'P','Q':'R','S':'T','U':'V','W':'X',
	'Y':'Z'}
message = list(input("Write the message: ").upper())
for symbol in range(len(message)):
	for key in keys:
		if message[symbol] == key:
			message[symbol] = keys[key]
		elif message[symbol] == keys[key]:
			message[symbol] = key
		else: pass
print("Final message:","".join(message))