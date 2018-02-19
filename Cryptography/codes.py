tupleWord = ('AND','THE','OR','ALL','ANY','WHAT','WHY','YES','NO',
'ONE','YOU','HE','SHE','USE','IF','ELSE','THIS','THAN','YOUR',
'ON','HOW','ARE','ME','IT','IS','THAT','WAS','OF','BE','OK')

tupleCode = ('!','@','#','$','%','^','&','*','(',')','-','_',
'+','=','/','?','<','>',';',':','{','}','[',']','~',',','.',
'"','|','\\')

keys = dict(zip(tupleWord, tupleCode))

cryptMode = input("[E]ncrypt|[D]ecrypt: ").upper()
if cryptMode not in ['E','D']:
	print("Error: mode is not Found!"); raise SystemExit

startMessage = input("Write the message: ").upper()

def encryptDecrypt(mode, message):
	for key in keys:
		if mode == 'E':
			if key in message:
				message = message.replace(key,keys[key])
		else:
			if keys[key] in message:
				message = message.replace(keys[key],key)
	return message
print("Final message:",encryptDecrypt(cryptMode, startMessage))