from os import remove
from os.path import splitext

from re import findall
from random import choice, randint

from pyAesCrypt import encryptFile, decryptFile
from rsa import newkeys, encrypt, PublicKey, decrypt, PrivateKey

def getNumbers(text):
    template = r"[0-9]+"
    return findall(template, text)

def getTwoSymbols(text):
    template = r"[A-Z]{2}"
    return findall(template, text)
    
### A1Z26 ###
def a1z26(mode, message, final = ""):
    message = message.upper()
    alpha = tuple("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    if mode == 'E': 
        for symbol in message:
            if symbol not in [chr(x) for x in range(65,91)]:
                message = message.replace(symbol, '')
        for symbol in message:
            final += "%hu "%(alpha.index(symbol)+1)
    else: 
        for number in getNumbers(message):
            final += "%s"%alpha[int(number)-1]
    return final

### ADFGVX ###
def adfgvx_stageOne(mode, message, final = ""):
    keyStageOne = {
        'A':'AA','N':'FD','0':'VF',
        'B':'AD','O':'FF','1':'VG',
        'C':'AF','P':'FG','2':'VV',
        'D':'AG','Q':'FV','3':'VX',
        'E':'AV','R':'FX','4':'XA',
        'F':'AX','S':'GA','5':'XD',
        'G':'DA','T':'GD','6':'XF',
        'H':'DD','U':'GF','7':'XG',
        'I':'DF','V':'GG','8':'XV',
        'J':'DG','W':'GV','9':'XX',
        'K':'DV','X':'GX',
        'L':'DX','Y':'VA',
        'M':'FA','Z':'VD'}
    if mode == 'E':
        for symbol in message:
            if symbol in keyStageOne:
                final += keyStageOne[symbol]
    else:
        for symbols in getTwoSymbols(message):
            for key in keyStageOne:
                if symbols == keyStageOne[key]:
                    final += key
    return final
def adfgvx_stageTwo(mode, keyStageTwo, message, final = ""):
    listCutWords = []
    if mode == 'E':
        while len(message) % len(keyStageTwo) != 0:
            message += 'XX'
        lengthList = len(message) // len(keyStageTwo)
        for _ in range(lengthList):
            listCutWords.append([])
        index = 0; counter = 1
        for symbol in message:
            if counter % len(keyStageTwo) != 0:
                listCutWords[index].append(symbol)
                counter += 1
            else:
                listCutWords[index].append(symbol)
                index += 1; counter = 1
        keys = {x:[] for x in keyStageTwo}
        index = 0
        for key in keyStageTwo:
            for x in range(len(listCutWords)):
                keys[key].append(listCutWords[x][index])
            index += 1
        keySort = list(keyStageTwo); keySort.sort()
        keys = {key:keys[key] for key in keySort if key in keys}
        for listSymbol in keys:
            for symbol in keys[listSymbol]:
                final += symbol
    else:
        keySort = list(keyStageTwo); keySort.sort()
        lengthList = len(message) // len(keyStageTwo)
        for _ in range(len(keyStageTwo)):
            listCutWords.append([])
        index = 0; counter = 1
        for symbol in message:
            if counter % lengthList != 0:
                listCutWords[index].append(symbol)
                counter += 1
            else:
                listCutWords[index].append(symbol)
                index += 1; counter = 1
        keys = {keySort[symbol]:listCutWords[symbol] for symbol in range(len(keySort))}
        keys = {key:keys[key] for key in keyStageTwo if key in keys}
        index = 0
        for _ in range(lengthList):
            for symbolOne in keys:
                final += keys[symbolOne][index]
            index += 1
    return final
def adfgvx(mode, message, key):
    mode, key, message = mode.upper(), key.upper(), message.upper()
    for symbol in key:
        if key.count(symbol) > 1:
            key = key.replace(symbol,'')
    for symbol in message:
        if symbol not in [chr(x) for x in range(65,91)]:
            message = message.replace(symbol,'')
    if mode == 'E':
        message = adfgvx_stageOne(mode, message)
        message = adfgvx_stageTwo(mode, key, message)
    else:
        message = adfgvx_stageTwo(mode, key, message)
        message = adfgvx_stageOne(mode, message)
    return message

### AES256-CBC ###
def aes(mode, file, password, final = ""):
    if mode == 'E':
        try: 
            encryptFile(str(file), str(file)+".crp", password, 64*1024)
            remove(file)
        except FileNotFoundError: return ":: File not found."
        else: return ":: File '{name}' overwritten.".format(name = str(file))
    else:
        try: 
            decryptFile(str(file), str(splitext(file)[0]), password, 64*1024)
            remove(file)
        except FileNotFoundError: return ":: File not found."
        except ValueError: return ":: Password is False."
        else: return ":: File '{name}' overwritten.".format(name = str(file))

### Affine ###
def affine(mode, message, key, final = ""):
    message = message.upper()
    key = key.split()
    for k in key:
        try: int(k)
        except: return "Only int numbers!"
    if len(key) != 2: return "Error: qualitity keys must be 2"
    for symbol in message:
            if mode == 'E': 
                final += chr((int(key[0]) * ord(symbol) + int(key[1]) - 13)%26 + ord('A'))
            else: 
                final += chr(pow(int(key[0]),11) * ((ord(symbol) + 26 - int(key[1]) - 13))%26 + ord('A'))
    return final

### Atbash ###
def atbash(message, final = ""):
    message = message.upper()
    alphaDefault = [chr(x) for x in range(65,91)]
    alphaReverse = list(alphaDefault); alphaReverse.reverse()
    for symbolMessage in message:
        for indexAlpha, symbolAlpha in enumerate(alphaDefault):
            if symbolMessage == symbolAlpha:
                final += alphaReverse[indexAlpha]
    return final

### Bacon ###
def bacon_regular(text):
    template = r"[A-Z]{5}"
    return findall(template, text)
def bacon(mode, message, final = ""):
    keys = {
        'A':"AAAAA", 'B':"AAAAB", 'C':"AAABA",
        'D':"AAABB", 'E':"AABAA", 'F':"AABAB",
        'G':"AABBA", 'H':"AABBB", 'I':"ABAAA",
        'J':"ABAAB", 'K':"ABABA", 'L':"ABABB",
        'M':"ABBAA", 'N':"ABBAB", 'O':"ABBBA",
        'P':"ABBBB", 'Q':"BAAAA", 'R':"BAAAB",
        'S':"BAABA", 'T':"BAABB", 'U':"BABAA",
        'V':"BABAB", 'W':"BABBA", 'X':"BABBB",
        'Y':"BBAAA", 'Z':"BBAAB", ' ':"BBABA"}
    message = message.upper()
    if mode == 'E':
        for symbol in message:
            if symbol in keys: final += keys[symbol]
    else:
        for symbolsFive in bacon_regular(message):
            for key in keys:
                if symbolsFive == keys[key]: final += key
    return final

### Book ###
def book(mode, message, key, final = ""):
    with open(key) as bookKey:
        book = bookKey.read()
    if mode == 'E':
        for symbolMessage in message:
            listIndexKey = []
            for indexKey, symbolKey in enumerate(book):
                if symbolMessage == symbolKey:
                    listIndexKey.append(indexKey)
            try:final += str(choice(listIndexKey)) + '/'
            except IndexError: pass
    else:
        for numbers in getNumbers(message):
            for indexKey, symbolKey in enumerate(book):
                if numbers == str(indexKey):
                    final += symbolKey
    return final    

### Caesar ###
def caesar(mode, message, key, final = ""):
    message = message.upper()
    try: key = int(key)
    except: return ":: Only int numbers."
    for symbol in message:
        if mode == 'E': 
            final += chr((ord(symbol) + key - 13)%26 + ord('A'))
        else: 
            final += chr((ord(symbol) - key - 13)%26 + ord('A'))
    return final

### CaesarS ###
def caesarS_remove(alpha, string):
    for symbol in string:
        if symbol in alpha: alpha.remove(symbol)
    for symbol in string:
        if symbol not in [chr(x) for x in range(65,91)] \
        or string.count(symbol) > 1: string.remove(symbol) 
    return alpha, string
def caesarS_insert(alpha_string, key):
    for index, symbol in enumerate(alpha_string[1]):
        alpha_string[0].insert((+index)%26, symbol)
    return alpha_string[0]
def caesarS(mode, message, key, final = "", alpha = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")):
    message = message.upper(); key = key.split()
    try: key[0] = int(key[0])
    except: return ":: Only int numbers."
    key[1] = key[1].upper()
    alpha = caesarS_insert(caesarS_remove(alpha, key[1]), key[0])
    for symbol in message:
        if mode == 'E':
            final += alpha[(alpha.index(symbol) + key[0])%26]
        else: 
            final += alpha[(alpha.index(symbol) - key[0])%26]
    return final

### Codes ###
def codes(mode, message):
    tupleWord = ('AND','THE','OR','ALL','ANY','WHAT','WHY','YES','NO',
    'ONE','YOU','HE','SHE','USE','IF','ELSE','THIS','THAN','YOUR',
    'ON','HOW','ARE','ME','IT','IS','THAT','WAS','OF','BE','OK')
    tupleCode = ('!','@','#','$','%','^','&','*','(',')','-','_',
    '+','=','/','?','<','>',';',':','{','}','[',']','~',',','.',
    '"','|','\\')
    keys = dict(zip(tupleWord, tupleCode))
    message = message.upper()
    for key in keys:
        if mode == 'E':
            if key in message:
                message = message.replace(key,keys[key])
        else:
            if keys[key] in message:
                message = message.replace(keys[key],key)
    return message

### Couples ###
def couples(message):
    keys = {
        'A':'B','C':'D','E':'F','G':'H','I':'J','K':'L',
        'M':'N','O':'P','Q':'R','S':'T','U':'V','W':'X',
        'Y':'Z'}
    message = list(message.upper())
    for symbol in range(len(message)):
        for key in keys:
            if message[symbol] == key:
                message[symbol] = keys[key]
            elif message[symbol] == keys[key]:
                message[symbol] = key
    return "".join(message)


### Double Cifir ###
def doubleCifir(mode, message, key, final = ''):
    message = list(message.upper())
    if mode == 'E':
        key = []
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
        return final + '\n' + '.'.join(key)
    else:
        listHalf = [
[message[x] for x in range(len(message)) if x%2 != 0],
[message[y] for y in range(len(message)) if y%2 == 0]]
        key = [int(x) for x in getNumbers(key)]
        keys = {y:[listHalf[0][x],listHalf[1][x]] for x,y in enumerate(key)}
        finalList = [
[keys[x][0] for x in range(len(keys)) if x in keys],
[keys[y][1] for y in range(len(keys)) if y in keys]]
        for i in range(2):
            for index in range(len(message)//2):
                final += finalList[i][index]
        return final

### Fence ###
def fence(mode, message, final = ""):
    if mode == 'E':
        encryptList = [
[message[x] for x in range(len(message)) if x%2 == 0],
[message[x] for x in range(len(message)) if x%2 != 0]
]
        for index in range(len(encryptList)):
            final += "".join(encryptList[index])
    else:
        if len(message)%2 != 0: message += " "
        length, half = len(message), len(message)//2
        decryptList = [
[message[x] for x in range(half)],
[message[x] for x in range(half,length)]
]
        for index in range(half):
            final += decryptList[0][index]+decryptList[1][index]
    return final

### Great Cipher ###
def greatcipher_regular(text):
        template = r"[0-9]{3}"
        return findall(template, text)
def greatcipher(mode, message, string = "", final = ""):
    message = message.upper()
    Limit = 350; Key = (
    '275','078','276','230','343','127','006','325','307','102',
    '334','185','004','002','008','283','277','260','256','305',
    '300','143','159','248','160','309','104','222','136','317',
    '264','053','218','137','177','315','301','244','040','072',
    '023','182','323','154','076','048','213','330','109','164',
    '257','179','043','166','207','240','220','205','228','073',
    '017','093','186','027','157','080','009','195','289','278',
    '116','238','028','271','058','001','132','236','044','029',
    '282','339','131','069','100','107','255','135','226','198',
    '335','035','187','119','293','133','270','347','097','273',

    '068','250','311','140','212','120','024','303','188','103',
    '209','114','034','267','061','184','261','225','349','167',
    '059','106','272','168','326','165','269','279','019','247',
    '087','156','239','088','092','026','071','304','241','180',
    '306','284','310','065','021','234','162','202','060','047',
    '039','318','321','152','117','324','067','348','031','308',
    '265','070','181','077','217','041','032','124','125','290',
    '235','037','231','003','342','158','020','322','216','091',
    '176','079','199','259','129','138','113','099','312','215',
    '115','145','122','193','254','314','153','344','123','340',

    '292','101','083','286','262','183','121','237','242','249',
    '246','139','018','042','295','178','245','022','148','163',
    '052','233','189','229','090','000','341','015','346','336',
    '082','345','281','036','005','089','038','064','141','046',
    '151','062','266','243','010','287','066','149','030','095',
    '147','171','173','332','055','045','253','298','227','299',
    '051','170','331','280','224','011','111','105','112','130',
    '192','268','169','128','033','098','075','194','211','085',
    '223','025','296','196','155','320','054','126','174','108',
    '118','144','172','302','146','294','190','012','210','086',

    '191','014','208','142','084','337','203','219','201','327',
    '197','057','221','016','338','206','333','134','150','063',
    '251','291','313','285','204','274','319','013','056','328',
    '214','263','200','096','288','007','252','161','050','110',
    '329','049','258','081','094','074','297','316','232','175',
    )
    keysCrypt = {
        'A':Key[0:8],     'B':Key[8:10],
        'C':Key[10:13],   'D':Key[13:17],
        'E':Key[17:29],   'F':Key[29:31],
        'G':Key[31:33],   'H':Key[33:39],
        'I':Key[39:45],   'J':[Key[45]],
        'K':[Key[46]],    'L':Key[47:51],
        'M':Key[51:53],   'N':Key[53:59],
        'O':Key[59:66],   'P':Key[66:68],
        'Q':[Key[68]],    'R':Key[69:75],
        'S':Key[75:81],   'T':Key[81:90],
        'U':Key[90:93],   'V':[Key[93]],
        'W':Key[94:96],   'X':[Key[96]],
        'Y':Key[97:99],   'Z':[Key[99]],
        ' ':Key[100:118]
    }
    listWord = ('TO','WHY','WITH','WAR','NOT','IN','OR','ELSE','THE','THAT','BY',
    'AND','HOW','BUT','IF','ONE','YOU','ME','USE','HIS','YOUR','ON','OF','WAS','BE',
    'THIS','WHAT','THEY','NO','YES','TRUE','FALSE','CALL','FEEL','CLOSE','VERY',
    'WHICH','CAR','ANY','HOLD','WORK','RUN','NEVER','START','EVEN','LIGHT','THAN',
    'AFTER','PUT','STOP','OLD','WATCH','FIRST','MAY','TALK','ANOTHER','BEHIND',
    'CUT','MEAN','SMILE','OUR','MUCH','IT','HE','SHE','ITS','HOUSE','KEEP','YEAH',
    'PLACE','BEGIN','NOTHING','YEAR','MAN','WOMAN','BECAUSE','THREE','SEEM','ARE',
    'WAIT','NEED','LAST','LATE','SURE','BIG','SMALL','FRONT','REALLY','NAME','ALL',
    'NEW','GUY','ANYTHING','SHOULD','KILL','POINT','WALL','BLACK','STEP','SECOND',
    'LIFE','MAYBE','FALL','OWN','FAR','WHILE','FOR','HELP','END','THOSE','SAME',
    'REACH','GIRL','STREET','NEXT','FEW','FEET','SHOW','MUST','TABLE','OK','IS',
    'OKAY','BODY','PHONE','ADD','WATER','FIRE','INSIDE','BREAK','EVER','SHAKE',
    'MEET','GREAT','MIND','ENOUGH','MINUTE','FOLLOW','ATTACK','DEAD','ALMOST')
    position = 118
    keysCode = {listWord[x]:Key[x + position] for x in range(len(listWord))}
    listSyllables = ('TH','WH','EE','AI','OO','IS','ING','ED','BE','ON','OR','ER',
    'CH','SH','GH','EN','EA','OU','LL','US','SE','AL','ST','EV','WO','UI','IN','RE',
    '!','?','.',',','@','#','$','%','*','^','-','+','=','/',':',';','&','~')
    position = len(listWord) + 118
    keysSyllables = {listSyllables[x]:Key[x + position] for x in range(len(listSyllables))}
    listSpecial = ('<-','->','<+','+>')
    position = len(listWord) + len(listSyllables) + 118
    keysSpecial = {listSpecial[x]:Key[x + position] for x in range(len(listSpecial))}
    position = len(listWord) + len(listSyllables) + len(listSpecial) + 118
    traps = tuple([Key[x] for x in range(position, Limit)])
    del listWord, listSpecial, position
    if mode == 'E':
        secondText = findall(r"[^\s]+", message)
        del message
        for indexWord in range(len(secondText)):
            if secondText[indexWord] in keysSpecial:
                secondText[indexWord] = keysSpecial[secondText[indexWord]]
        for indexWord in range(len(secondText)):
            if secondText[indexWord] in keysCode:
                secondText[indexWord] = keysCode[secondText[indexWord]]
        for indexWord in range(len(secondText)):
            for syllable in keysSyllables:
                if syllable in secondText[indexWord]:
                    secondText[indexWord] = secondText[indexWord].replace(syllable,keysSyllables[syllable])
        for indexWord in range(len(secondText)):
            secondText[indexWord] = list(secondText[indexWord])
        for indexWord in range(len(secondText)):
            secondText[indexWord].append(' ')
        for indexWord in range(len(secondText)):
            for indexSymbol in range(len(secondText[indexWord])):
                symbol = secondText[indexWord][indexSymbol]
                if symbol in keysCrypt:
                    length = len(keysCrypt[symbol])
                    secondText[indexWord][indexSymbol] = keysCrypt[symbol][randint(0, length - 1)]
        for word in secondText:
            string += "".join(word)
        finalList = list(greatcipher_regular(string))
        for indexList in range(len(finalList)):
            randSwitch = randint(0,2); randPosition = randint(0,len(finalList))
            if not randSwitch: finalList.insert(randPosition,choice(traps))
        for word in finalList:
            final += "".join(word)
        return ".".join(greatcipher_regular(final))
    else:
        for symbolText in greatcipher_regular(message):
            for element in keysSpecial: # Перебор всех специальных символов
                if symbolText == keysSpecial[element]: final += element
            for word in keysCode: # Перебор всех кодов
                if symbolText == keysCode[word]: final += word
            for syllable in keysSyllables: # Перебор всех слогов
                if symbolText == keysSyllables[syllable]: final += syllable
            for symbol in keysCrypt: # Перебор всех шифров
                if symbolText in keysCrypt[symbol]: final += symbol
        listWord = findall(r"[^\s]+",final)
        for _ in range(len(listWord)):
            for element in keysSpecial:
                if element in listWord:
                    if element == '<-':
                        del listWord[listWord.index(element) - 1]
                        listWord.remove(element)
                    elif element == '->':
                        del listWord[listWord.index(element) + 1]
                        listWord.remove(element)
                    elif element == '<+':
                        listWord[listWord.index(element)] = listWord[listWord.index(element) - 1]
                    elif element == '+>':
                        listWord[listWord.index(element)] = listWord[listWord.index(element) + 1]
                    else: pass
        final = " ".join(listWord)
    return final

### Gronsfeld ###
def gronsfeld(mode, message, key, final = ""):
    message = message.upper()
    try: int(key)
    except: return ":: Only int numbers."
    key *= len(message) // len(key) + 1
    for index, symbol in enumerate(message):
        if mode == 'E':
            temp = ord(symbol) + int(key[index]) -13
        else:
            temp = ord(symbol) - int(key[index]) -13
        final += chr(temp%26 + ord('A'))
    return final

### Hill[2x2] ###
def hill2x2_crypt(message, matrix, summ = 0, final = ""):
    alpha = tuple("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    for double in range(len(message)):
        for string in range(2):
            for column in range(2):
                summ += matrix[string][column] * alpha.index(message[double][column])
            final += alpha[(summ)%26]; summ = 0
    return final
def hill2x2(mode, message, matrix):
    message = message.upper(); matrix = matrix.split()
    for symbol in message:
        if symbol not in [chr(x) for x in range(65,91)]:
            message = message.replace(symbol,'')
    while len(message) % 2 != 0: message += 'Z'
    matrix = [int(x) for x in matrix]
    matrix = [matrix[:2],matrix[2:]]
    det = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    if det != 1: return ":: Determinant != 1."
    imatrix = [
        [matrix[1][1],-matrix[0][1]],
        [-matrix[1][0],matrix[0][0]]]
    if mode == 'E': return hill2x2_crypt(getTwoSymbols(message), matrix)
    else: return hill2x2_crypt(getTwoSymbols(message), imatrix)

### Hill[3x3] ###
def checkErrors(key, alpha):
    if len(key) != 9: return "Error: len(key) != 9"
    elif getDeter(sliceto(key, alpha)) == 0: return "Error: det(Key) = 0"
    elif getDeter(sliceto(key, alpha)) % 2 == 0: return "Error: det(Key) mod 2 = 0"
    elif getDeter(sliceto(key, alpha)) % 13 == 0: return "Error: det(Key) mod 13 = 0"
    else: return None
def regular(text): 
    template = r"[A-Z]{3}"
    return findall(template, text)
def encode(matrix, alpha): 
    for x in range(len(matrix)):
        for y in range(3):
            matrix[x][y] = alpha.index(matrix[x][y])
    return matrix
def decode(matrixM, matrixK, alpha, message = ""):
    matrixF = []
    for z in range(len(matrixM)):
        temp = [0,0,0]
        for x in range(3):
            for y in range(3):
                temp[x] += matrixM[z][y] * matrixK[x][y]
            temp[x] = alpha[temp[x] % 26]
        matrixF.append(temp)
    for string in matrixF: message += "".join(string)
    return message
def sliceto(text, alpha): 
    matrix = []
    for three in regular(text): matrix.append(list(three))
    return encode(matrix, alpha)
def algebratic(x, y, det, key, alpha): 
    matrix = sliceto(key, alpha)
    matrix.remove(matrix[x])
    for z in range(2):
        matrix[z].remove(matrix[z][y])
    iM = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    return (pow(-1, x + y) * iM * det) % 26
def getDeter(matrix):
    return \
    matrix[0][0] * matrix[1][1] * matrix[2][2] - matrix[0][0] * matrix[1][2] * matrix[2][1] - \
    matrix[0][1] * matrix[1][0] * matrix[2][2] + matrix[0][1] * matrix[1][2] * matrix[2][0] + \
    matrix[0][2] * matrix[1][0] * matrix[2][1] - matrix[0][2] * matrix[1][1] * matrix[2][0]
def getAlgbr(det, key, alpha):
    algbrs = [0 for _ in range(9)]; index = 0
    for string in range(3):
        for column in range(3):
            algbrs[index] = algebratic(string, column, det, key, alpha); index += 1
    return algbrs
def getIMatr(algbr):
    return [
        [algbr[0],algbr[3],algbr[6]],
        [algbr[1],algbr[4],algbr[7]],
        [algbr[2],algbr[5],algbr[8]]
    ]
def hill3x3(mode, message, key, final = ""):
    message = message.upper()
    alpha = tuple("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    for symbol in message:
        if symbol not in alpha:
            message = message.replace(symbol,'')
    while len(message) % 3 != 0: message += 'Z'
    MatrixMessage, MatrixKey = sliceto(message, alpha), sliceto(key, alpha)
    if checkErrors(key, alpha): return checkErrors(key, alpha)
    if mode == 'E':
        final = decode(MatrixMessage, MatrixKey, alpha)
    else:
        deter = getDeter(MatrixKey); algbr = getAlgbr(deter, key, alpha)
        final = decode(MatrixMessage, getIMatr(algbr), alpha)
    return final

### Homophonic ###
def homophonic(mode, message, final = ""):
    values = ('1','2','3','4','5','6','7','8','9','0','a','b','c',\
    'd','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s',\
    't','u','v','w','x','y','z','!','@','\\','#','№','$',';','%','^',\
    ':','&','?','(',')','-','_','+','=','`','~','[',']','{',\
    '}','.',',','/','|','A','B','C','D','E','F','G','H','J','K','L',\
    'M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','<',\
    '>','А','М','В','С','у','Е','Т','а','Х','З')
    dictHom = {
        'A':values[0:8],    'B':values[8:10],
        'C':values[10:13],  'D':values[13:17],
        'E':values[17:29],  'F':values[29:31],
        'G':values[31:33],  'H':values[33:39],
        'I':values[39:45],  'J':[values[45]],
        'K':[values[46]],   'L':values[47:51],
        'M':values[51:53],  'N':values[53:59],
        'O':values[59:66],  'P':values[66:68],
        'Q':[values[68]],   'R':values[69:75],
        'S':values[75:81],  'T':values[81:90],
        'U':values[90:93],  'V':[values[93]],
        'W':values[94:96],  'X':[values[96]],
        'Y':values[97:99],  'Z':[values[99]]
    }
    if mode == 'E':
        for symbol in message.upper():
            if symbol in dictHom: final += choice(dictHom[symbol])
    else:
        for symbol in message:
            for key in dictHom:
                if symbol in dictHom[key]: final += key
    return final

### Lattice ###
def lattice(message):
    pass

### Playfair ###
def playfair(mode, message, final = ""):
    matrix = [
        ['S','O','M','E','T'],
        ['H','I','N','G','A'],
        ['B','C','D','F','K'],
        ['L','P','Q','R','U'],
        ['V','W','X','Y','Z']
    ]; addSymbol = 'X'
    message = list(message.upper())
    if mode == 'E':
        for symbol in message:
            if symbol not in [chr(x) for x in range(65,91)]:
                message.remove(symbol)
        for index in range(len(message)):
            if message[index] == 'J': message[index] = 'I'
        for index in range(1,len(message)):
            if message[index] == message[index - 1]:
                message.insert(index,addSymbol)
        if len(message) % 2 != 0:
            message.append(addSymbol)
    binaryList = getTwoSymbols("".join(message))
    for binary in range(len(binaryList)):
        binaryList[binary] = list(binaryList[binary])
        for indexString in range(len(matrix)):
            for indexSymbol in range(len(matrix[indexString])):
                if binaryList[binary][0] == matrix[indexString][indexSymbol]:
                    y0, x0 = indexString, indexSymbol
                if binaryList[binary][1] == matrix[indexString][indexSymbol]:
                    y1, x1 = indexString, indexSymbol
        for indexString in range(len(matrix)):
            if matrix[y0][x0] in matrix[indexString] and matrix[y1][x1] in matrix[indexString]:
                if mode == 'E':
                    x0 = x0 + 1 if x0 != 4 else 0
                    x1 = x1 + 1 if x1 != 4 else 0
                else:
                    x0 = x0 - 1 if x0 != 0 else 4
                    x1 = x1 - 1 if x1 != 0 else 4
        y0,y1 = y1,y0
        binaryList[binary][0] = matrix[y0][x0]
        binaryList[binary][1] = matrix[y1][x1]
    for binary in range(len(binaryList)):
        for symbol in binaryList[binary]:
            final += symbol
    return final

### Polibiy ###
def polibiy(mode, message):
    final = []; message = message.upper()
    keys = {
        'A':'11', 'B':'12', 'C':'13', 'D':'14',
        'E':'15', 'F':'16', 'G':'21', 'H':'22',
        'I':'23', 'J':'24', 'K':'25', 'L':'26',
        'M':'31', 'N':'32', 'O':'33', 'P':'34',
        'Q':'35', 'R':'36', 'S':'41', 'T':'42',
        'U':'43', 'V':'44', 'W':'45', 'X':'46',
        'Y':'51', 'Z':'52', '0':'53', '1':'54',
        '2':'55', '3':'56', '4':'61', '5':'62',
        '6':'63', '7':'64', '8':'65', '9':'66'
    }
    if mode == 'E':
        for symbol in message:
            if symbol in keys:
                final.append(keys[symbol])
    else:
        for twoNumbers in getNumbers(message):
            for key in keys:
                if twoNumbers == keys[key]:
                    final.append(key)
    return ".".join(final)

### Ports ###
def ports_regular(mode, text):
    if mode == 'E': template = r"[A-Z]{2}"
    else: template = r"[0-9]{3}"
    return findall(template, text)
def ports(mode, message):
    final = []
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
    message = message.upper()
    if mode == 'E':
        for symbol in message:
            if symbol not in [chr(x) for x in range(65,91)]:
                message = message.replace(symbol,'')
        if len(message)%2 != 0: message += 'Z'
        for symbols in ports_regular(mode, message):
            for key in cryptKeys:
                if symbols == cryptKeys[key]:
                    final.append(key)
    else:
        for number in ports_regular(mode, message):
            if number in cryptKeys:
                final.append(cryptKeys[number])
    return ".".join(final)

### PowVishener ###
def powVishener(mode, message, keys):
    message = message.upper()
    keys = keys.upper(); keys = keys.split()
    for key in keys:
        final = ""
        key *= len(message) // len(key) + 1
        for index, symbol in enumerate(message):
            if mode == 'E':
                temp = ord(symbol) + ord(key[index])
            else:
                temp = ord(symbol) - ord(key[index])
            final += chr(temp % 26 + ord('A'))
        message = final
    return final

### Psevdo ###
def psevdo_regular(text):
    template = r"\w{3}"
    return findall(template, text)
def psevdo(mode, message, final = ""):
    keys = {
        'A':"AAA", 'B':"AAА", 'C':"AAΑ",
        'D':"AАA", 'E':"AАА", 'F':"AАΑ",
        'G':"AΑA", 'H':"AΑА", 'I':"AΑΑ",
        'J':"АAA", 'K':"АAА", 'L':"АAΑ",
        'M':"ААA", 'N':"ААА", 'O':"ААΑ",
        'P':"АΑA", 'Q':"АΑА", 'R':"АΑΑ",
        'S':"ΑAA", 'T':"ΑAА", 'U':"ΑAΑ",
        'V':"ΑАA", 'W':"ΑАА", 'X':"ΑАΑ",
        'Y':"ΑΑA", 'Z':"ΑΑА", ' ':"ΑΑΑ"
    }
    if mode == 'E':
        message = message.upper()
        for symbol in message:
            if symbol in keys:
                final += keys[symbol]
    else:
        for threeSymbols in psevdo_regular(message):
            for key in keys:
                if threeSymbols == keys[key]:
                    final += key
    return final

### Replace ###
def replace(mode, message, final = ""):
    message = message.upper()
    symbolsAlpha = [chr(x) for x in range(65,91)]
    symbolsCrypt = ('!','@','#','$','%','^','&','*','(',')','-','=',
    '+','?',':',';','<','>','/','[',']','{','}','|','.',',','~')
    keys = dict(zip(symbolsAlpha,symbolsCrypt))
    if mode == 'E':
        for symbol in message:
            if symbol in keys: final += keys[symbol]
    else:
        for symbol in message:
            for key in keys:
                if symbol == keys[key]: final += key
    return final

### ROT13 ###
def rot13(message):
    message = list(message.upper())
    for symbol in range(len(message)):
        message[symbol] = chr(ord(message[symbol])%26+ord('A'))
    return "".join(message)

### Rotors ###
def rotors(mode, message, final = ""):
    message = message.upper()
    rotors = (
        (10,24,14,12,23,2,7,15,24,2,7,5,22,6,2,1,22,12,6,9,7,2,11,23,14,2),
        (1,7,11,26,12,5,11,20,11,7,18,6,17,18,19,1,13,5,2,9,11,13,6,17,26,24),
        (9,1,21,6,4,19,25,6,17,10,26,1,23,6,1,17,19,17,25,21,3,21,17,1,18,20)
    )
    x,y,z = 1,2,3
    for symbol in message:
        rotor = rotors[0][x] + rotors[1][y] + rotors[2][z]
        if mode == 'E':
            if symbol in [chr(x) for x in range(65,91)]:
                final += chr((ord(symbol) - 13 + rotor)%26 + ord('A'))
            else: continue
        else: 
            final += chr((ord(symbol) - 13 - rotor)%26 + ord('A'))
        if x != 25: x += 1
        else:
            x = 0
            if y != 25: y += 1
            else:
                y = 0
                if z != 25: z += 1
                else: z = 0
    return final

### RSA ###
def rsa(mode, message, key):
    if mode == 'E':
        message = message.encode("utf8")
        if not key:
            pub, priv = newkeys(1024)
            encryptMessage = encrypt(message, pub)
            return "%s\n%s\n%s"%(str(pub), str(priv), encryptMessage)
        else:
            encryptMessage = encrypt(message, eval(key))
            return str(encryptMessage)
    else:
        decryptMessage = decrypt(eval(message), eval(key))
        return decryptMessage

### Syllables ###
def syllables(mode, message):
    message = message.upper()
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
    if mode == 'E':
        for syllable in syllables:
            if syllable in message:
                message = message.replace(syllable,symbols[syllables.index(syllable)])
    else:
        for symbol in symbols:
            if symbol in message:
                message = message.replace(symbol, syllables[symbols.index(symbol)])
    return message

### Tarabar ###
def tarabar(message):
    keys = {
    'B':'Z','C':'X','D':'W','F':'V','G':'T',
    'H':'S','J':'R','K':'Q','L':'P','M':'N'}
    message = list(message.upper())
    for symbol in range(len(message)):
        for key in keys:
            if message[symbol] == key:
                message[symbol] = keys[key]
            elif message[symbol] == keys[key]:
                message[symbol] = key
            else: pass
    return "".join(message)

### Thritemius ###
def thritemius(mode, message, key, final = ""):
        message = list(message.upper())
        for symbol in message:
            if symbol not in [chr(x) for x in range(65,91)]:
                message.remove(symbol)
        key = eval('lambda x: ' + key) # x*2
        for index, symbol in enumerate(message):
            if mode == 'E':
                temp = ord(symbol) + key(index) - 13
            else:
                temp = ord(symbol) - key(index) - 13
            final += chr(temp%26 + ord('A'))
        return final

### Typex ###
def typex_stageOne(message):
    switch = {
        'H':'Z', 'S':'N', 'L':'M',
        'P':'Q', 'R':'W', 'X':'Y'}
    message = list(message)
    for symbol in range(len(message)):
        for key in switch:
            if message[symbol] == key:
                message[symbol] = switch[key]
            elif message[symbol] == switch[key]:
                message[symbol] = key
    return "".join(message)
def typex_stageTwo(mode, message, final = ""):
    rotors = (
        (10,24,14,12,23,2,7,15,24,2,7,5,22,6,2,1,22,12,6,9,7,2,11,23,14,2),
        (1,7,11,26,12,5,11,20,11,7,18,6,17,18,19,1,13,5,2,9,11,13,6,17,26,24),
        (9,1,21,6,4,19,25,6,17,10,26,1,23,6,1,17,19,17,25,21,3,21,17,1,18,20)
    )
    X,Y,Z = 2,0,1; x,y,z = 1,2,3
    for symbol in message:
        rotor = rotors[X][x] + rotors[Y][y] + rotors[Z][z]
        if mode == 'E':
            if symbol in [chr(x) for x in range(65,91)]:
                final += chr((ord(symbol) - 13 + rotor)%26 + ord('A'))
            else: continue
        else: 
            final += chr((ord(symbol) - 13 - rotor)%26 + ord('A'))
        if x != 25: x += 1
        else:
            x = 0
            if y != 25: y += 1
            else:
                y = 0
                if z != 25: z += 1
                else: z = 0
    return final
def typex(mode, message):
    message = message.upper()
    if mode == 'E': 
        message = typex_stageOne(message)
        message = typex_stageTwo(mode, message)
    else: 
        message = typex_stageTwo(mode, message)
        message = typex_stageOne(message)
    return message

### Vernam ###
def vernam(mode, message, key, final = ""):
    message = message.upper(); keys = []
    if mode == 'E':
        for symbol in message:
            key = randint(0,25); keys.append(str(key))
            final += chr((ord(symbol) + key - 13)%26 + ord('A'))
        return final + '\n' + '.'.join(keys)
    else: 
        for index, symbol in enumerate(message):
            final += chr((ord(symbol) - int(getNumbers(key)[index]) - 13)%26 + ord('A'))
        return final

### Vishener ###
def vishener(mode, message, key, final = ""):
    message = message.upper(); key = key.upper();
    key *= len(message) // len(key) + 1
    for index, symbol in enumerate(message):
        if mode == 'E':
            temp = ord(symbol) + ord(key[index])
        else:
            temp = ord(symbol) - ord(key[index])
        final += chr(temp % 26 + ord('A'))
    return final

### XOR ###
def xor(message, key):
    message = list(message)
    for symbol in range(len(message)):
        try: message[symbol] = chr(ord(message[symbol]) ^ int(key))
        except ValueError: message[symbol] = chr(ord(message[symbol]) ^ ord(key))
    return "".join(message)
