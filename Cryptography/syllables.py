syllables = ('TH','EE','OO','ING','ED','SS','DE','RE','AR',
'WH','AI','IS','BE','CH','SH','GH','EN','OU','LL','HE','US',
'ST','EV','WO','UI','IN','ER','OR','AT','RD','AL','LE','LD',
'UR','UP','SO','ME','SE','MY','NA','TE','NE','VE','LA','GE',
'ON','GU','RA','AN','AG','SH','CR','FO','OW','PY','WR','CA',
'EA','SP','PR','AS','AU','MA','KE','UT','DO','NT','WA','HU',
'AD','WI','RI','LO','FU','BR','OF','AP','TO','IF','AM','ND',
'LY','TA','KN','FA','TT','LP')
symbols = ('!!$','@@2','#99','$$!','^^$','&<<','**?',';;{',
'||}','::#','--/','++;','//~','==]','[++','?::','>>&','//?',
'&**','!<<','%((','::>','<;;','*++','?//','^$$','~""','!::',
'::!','&??','//!','#$$','((:',':))','{[[','[[]',';;<','|[[',
'$??','0//','1[[','@]]','[[<',':]]',':[[',']::','.','!','@',
'#','$','%','^','&','*','(',')','-','_','=','+','{','}',':',
';','"',',','<','>','?','/','~','`','|','\\','[',']','1','2',
'3','4','5','6','7','8','9','0')
cryptMode = input("[E]ncrypt|[D]ecrypt: ").upper()
if cryptMode not in ['E','D']:
	print("Error: mode is not Found!"); raise SystemExit
startMessage = input("Write the message: ").upper()
def encryptDecrypt(mode, message):
	if mode == 'E':
		for syllable in syllables:
			if syllable in message:
				message = message.replace(syllable,symbols[syllables.index(syllable)])
	else:
		for symbol in symbols:
			if symbol in message:
				message = message.replace(symbol, syllables[symbols.index(symbol)])
	return message
print("Final message:",encryptDecrypt(cryptMode, startMessage))