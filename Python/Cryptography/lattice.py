from random import choice, randint

squade = 10

alphaList = [chr(x) for x in range(65,91)] + [chr(y) for y in range(97,123)]
stringList = [choice(alphaList) for _ in range(squade*squade)]

def getKey(text):
	while True:
		keys = [randint(0,99) for _ in range(len(text))]
		for number in keys:
			switch = False
			if keys.count(number) > 1:
				switch = True; break
		if switch == False:
			return keys

def lattice(index = 0):
	print(end = '    ')
	for string in range(squade):
		print(string, end = '   ')
	for string in range(squade):
		print()
		for column in range(squade):
			if index%squade == 0:
				print(index//squade, end = ' | ')
			print(stringList[index], end = ' | ')
			index += 1
	print()

message = input("Write the message: ")
keyList = getKey(message)

keyList.sort()
print("Keys:",keyList)

for index, symbol in enumerate(message):
	del stringList[keyList[index]]
	stringList.insert(keyList[index],symbol)
lattice()