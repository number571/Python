cryptMessage = input("Write the message: ").upper()
print("All possible variants of decrypt:")
for key in range(26):
	if key < 10: print("[ 0%d ]"%(key), end = ' ')
	else: print("[ %d ]"%(key), end = ' ')
	for symbol in cryptMessage:
		print(chr((ord(symbol)-key-13)%26+ord('A')), end = '')
	print()