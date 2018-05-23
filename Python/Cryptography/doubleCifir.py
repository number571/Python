from re import findall
from random import choice
cryptMode = input("[E]ncrypt|[D]ecrypt: ").upper()
if cryptMode not in ['E','D']:
	print("Error: mode is not Found!"); raise SystemExit
startMessage = list(input("Write the message: ").upper())
def regular(text):
	template = r"[0-9]+"
	return findall(template, text)
def encryptDecrypt(mode, message, final = '', key = []):
	if mode == 'E':
		if len(message) % 2 != 0: message.append(' ')
		listHalf = [
[message[x] for x in range(len(message)//2, len(message))],
[message[y] for y in range(len(message)//2)]]
		keys = {x:[listHalf[0][x],listHalf[1][x]] for x in range(len(message)//2)}
		listKey = [x for x in range(len(keys))]
		newList = []
		for _ in range(len(keys)):
			choiceKey = choice(listKey); key.append(str(choiceKey))
			newList.append(keys[choiceKey]); listKey.remove(choiceKey)
		for listIndex in range(len(newList)):
			for symbol in newList[listIndex]:
				final += symbol
		return final, '.'.join(key)
	else:
		listHalf = [
[message[x] for x in range(len(message)) if x%2 != 0],
[message[y] for y in range(len(message)) if y%2 == 0]]
		key = regular(input("Write the key: "))
		key = [int(x) for x in key]
		keys = {y:[listHalf[0][x],listHalf[1][x]] for x,y in enumerate(key)}
		finalList = [
[keys[x][0] for x in range(len(keys)) if x in keys],
[keys[y][1] for y in range(len(keys)) if y in keys]]
		for i in range(2):
			for index in range(len(message)//2):
				final += finalList[i][index]
		return final
print("Final message:",encryptDecrypt(cryptMode, startMessage))