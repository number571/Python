from re import findall

stageOne = ['00'+str(x) for x in range(1,10)]
stageTwo = ['0'+str(x) for x in range(10,100)]
stageThree = [str(x) for x in range(100,676+1)]

N = tuple(stageOne + stageTwo + stageThree)

del stageOne, stageTwo, stageThree

coordinateX = tuple([chr(alpha) for alpha in range(65,91)])
coordinateY = tuple([chr(alpha) for alpha in range(65,91)])

cryptKeys = {x:None for x in N}
keys = tuple([key for key in cryptKeys])

counter = 0
for x in coordinateX:
	for y in coordinateY:
		cryptKeys[keys[counter]] = x + y
		counter += 1

del N, coordinateX, coordinateY, counter, keys

cryptMode = input("[E]ncrypt|[D]ecrypt: ").upper()
if cryptMode not in ['E','D']:
	print("Error: mode not in (E/D)")
	raise SystemExit
startMessage = input("Write the message: ").upper()

def regular(mode, text):
	if mode == 'E': template = r"[A-Z]{2}"
	else: template = r"[0-9]{3}"
	return findall(template, text)

def encryptDecrypt(mode, message, final = []):
	if mode == 'E':
		for symbol in message:
			if symbol not in [chr(x) for x in range(65,91)]:
				message = message.replace(symbol,'')
		if len(message)%2 != 0: message += 'Z'
		for symbols in regular(mode, message):
			for key in cryptKeys:
				if symbols == cryptKeys[key]:
					final.append(key)
	else:
		for number in regular(mode, message):
			if number in cryptKeys:
				final.append(cryptKeys[number])
	return ".".join(final)
print("Final message:",encryptDecrypt(cryptMode, startMessage))