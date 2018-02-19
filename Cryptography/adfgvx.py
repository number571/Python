from re import findall

cryptMode = input("[E]ncrypt|[D]ecrypt: ").upper()
if cryptMode not in ['E','D']:
    print("Error: mode is not Found!"); raise SystemExit
startMessage = input("Write the message: ").upper()
keyStageTwo = list(input("Write the key: ").upper())
for symbol in keyStageTwo:
    if keyStageTwo.count(symbol) > 1:
        keyStageTwo.remove(symbol)

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
'M':'FA','Z':'VD',
}

def regular(text):
    template = r"[A-Z]{2}"
    return findall(template, text)

def stageOne(mode, message, final = ""):
    if mode == 'E':
        for symbol in message:
            if symbol in keyStageOne:
                final += keyStageOne[symbol]
    else:
        for symbols in regular(message):
            for key in keyStageOne:
                if symbols == keyStageOne[key]:
                    final += key
    return final

def stageTwo(mode, message, final = "", listCutWords = []):
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

def encryptDecrypt(mode, message):
    if mode == 'E':
        message = stageOne(mode, message)
        message = stageTwo(mode, message)
    else:
        message = stageTwo(mode, message)
        message = stageOne(mode, message)
    return message

print("Final message:",encryptDecrypt(cryptMode, startMessage))