message = list(input("Write the message: ").upper())
for symbol in range(len(message)):
	message[symbol] = chr(ord(message[symbol])%26+ord('A'))
print("Final message:", "".join(message))