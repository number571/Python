message = input("Write the message: ").upper()
alphaDefault = [chr(x) for x in range(65,91)]
alphaReverse = list(alphaDefault); alphaReverse.reverse()
final = ""
for symbolMessage in message:
	for indexAlpha, symbolAlpha in enumerate(alphaDefault):
		if symbolMessage == symbolAlpha:
			final += alphaReverse[indexAlpha]
print("Final message:", final)