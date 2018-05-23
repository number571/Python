from random import choice

values = ['1','2','3','4','5','6','7','8','9','0','a','b','c',\
'd','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s',\
't','u','v','w','x','y','z','!','@','\\','#','№','$',';','%','^',\
':','&','?','(',')','-','_','+','=','`','~','[',']','{',\
'}','.',',','/','|','A','B','C','D','E','F','G','H','J','K','L',\
'M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','<',\
'>','А','М','В','С','у','Е','Т','а','Х','З']

dictHom = {
	'A':values[0:8],	'B':values[8:10],
	'C':values[10:13],	'D':values[13:17],
	'E':values[17:29],	'F':values[29:31],
	'G':values[31:33],	'H':values[33:39],
	'I':values[39:45],	'J':[values[45]],
	'K':[values[46]],	'L':values[47:51],
	'M':values[51:53],	'N':values[53:59],
	'O':values[59:66],	'P':values[66:68],
	'Q':[values[68]],	'R':values[69:75],
	'S':values[75:81],	'T':values[81:90],
	'U':values[90:93],	'V':[values[93]],
	'W':values[94:96],	'X':[values[96]],
	'Y':values[97:99],	'Z':[values[99]]
}

cryptMode = input("[E]ncrypt|[D]ecrypt: ").upper()
if cryptMode not in ['E','D']:
	print("Error: mode is not Found!"); raise SystemExit
startMessage = input("Write the message: ")
def encryptDecrypt(mode, message, final = ""):
	if mode == 'E':
		for symbol in message.upper():
			if symbol in dictHom:
				final += choice(dictHom[symbol])
	else:
		for symbol in message:
			for key in dictHom:
				if symbol in dictHom[key]:
					final += key
	return final
print("Final message:",encryptDecrypt(cryptMode, startMessage))