from memory import Key, Limit
from random import randint, choice
from re import findall

############################################################################
# ---------------------- Омофоническое шифрование -------------------------#
# Количество занимаемого места памяти: 118
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

# -------------------------------------------------------------------------#

############################################################################
# ---------------------------- Кодирование --------------------------------#
# Количество занимаемого места памяти: 137
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

position = 118 # 118
keysCode = {listWord[x]:Key[x + position] for x in range(len(listWord))}
# -------------------------------------------------------------------------#

############################################################################
# ----------------------- Замена слогов и символов ------------------------#
# Количество занимаемого места памяти: 46
listSyllables = ('TH','WH','EE','AI','OO','IS','ING','ED','BE','ON','OR','ER',
'CH','SH','GH','EN','EA','OU','LL','US','SE','AL','ST','EV','WO','UI','IN','RE',
'!','?','.',',','@','#','$','%','*','^','-','+','=','/',':',';','&','~')

position = len(listWord) + 118 # 137 + 118 = 255
keysSyllables = {listSyllables[x]:Key[x + position] for x in range(len(listSyllables))}
# -------------------------------------------------------------------------#

############################################################################
# ------------------------ Специальные символы ----------------------------#
# Количество занимаемого места памяти: 4
listSpecial = ('<-','->','<+','+>')

position = len(listWord) + len(listSyllables) + 118 # 137 + 46 + 118 = 301
keysSpecial = {listSpecial[x]:Key[x + position] for x in range(len(listSpecial))}
# -------------------------------------------------------------------------#

############################################################################
# --------------------------- Ложные символы ------------------------------#
# 350 - (4 + 137 + 46 + 118) = 45
position = len(listWord) + len(listSyllables) + len(listSpecial) + 118

# Количество занимаемого места памяти: 45
traps = tuple([Key[x] for x in range(position, Limit)])
# -------------------------------------------------------------------------#

# Удаление неиспользуемых элементов
del listWord, listSpecial, position

# Опция шифрования/расшифрования
cryptMode = input("[E]ncrypt|[D]ecrypt: ").upper()
if cryptMode not in ['E','D']:
    print("Error: mode is not Found!"); raise SystemExit

# Открытое сообщение
startMessage = input("Write the message: ").upper()

# Функция с регулярным выражением разделения трёх чисел
def regular(text):
    template = r"[0-9]{3}"
    return findall(template, text)

def encryptDecrypt(mode, message, final = "", string = ""):
    ## Шифрование
    if cryptMode == 'E':
        # Разделение списка на слова
        secondText = findall(r"[^\s]+", message)

        # Удаление неиспользуемых элементов
        del message

        # Внедрение в код специальных символов
        for indexWord in range(len(secondText)):
            if secondText[indexWord] in keysSpecial:
                secondText[indexWord] = keysSpecial[secondText[indexWord]]

        # Кодирование слов на числа
        for indexWord in range(len(secondText)):
            if secondText[indexWord] in keysCode:
                secondText[indexWord] = keysCode[secondText[indexWord]]

        # Замена слогов на числа
        for indexWord in range(len(secondText)):
            for syllable in keysSyllables:
                if syllable in secondText[indexWord]:
                    secondText[indexWord] = secondText[indexWord].replace(syllable,keysSyllables[syllable])

        # Разделение всех слов на символы
        for indexWord in range(len(secondText)):
            secondText[indexWord] = list(secondText[indexWord])
        for indexWord in range(len(secondText)):
            secondText[indexWord].append(' ')

        # Шифрование всех символов на числа
        for indexWord in range(len(secondText)):
            for indexSymbol in range(len(secondText[indexWord])):
                symbol = secondText[indexWord][indexSymbol]
                if symbol in keysCrypt:
                    length = len(keysCrypt[symbol])
                    secondText[indexWord][indexSymbol] = keysCrypt[symbol][randint(0, length - 1)]

        # Соединение всех чисел в одну строку и разделение по три
        for word in secondText:
            string += "".join(word)
        finalList = list(regular(string))

        # Внедрение в код ложных символов
        for indexList in range(len(finalList)):
            randSwitch = randint(0,2); randPosition = randint(0,len(finalList))
            if not randSwitch: finalList.insert(randPosition,choice(traps))

        # Занесение в переменную final зашифрованный текст
        for word in finalList:
            final += "".join(word)
        return ".".join(regular(final))

    ## Расшифрование 
    else:
        # Перебор всех 'XYZ' чисел в зашифрованном сообщении
        for symbolText in regular(message):
            for element in keysSpecial: # Перебор всех специальных символов
                if symbolText == keysSpecial[element]: final += element
            for word in keysCode: # Перебор всех кодов
                if symbolText == keysCode[word]: final += word
            for syllable in keysSyllables: # Перебор всех слогов
                if symbolText == keysSyllables[syllable]: final += syllable
            for symbol in keysCrypt: # Перебор всех шифров
                if symbolText in keysCrypt[symbol]: final += symbol
        listWord = findall(r"[^\s]+",final)
            
        # Опции специальных символов
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

# Вывод финального сообщения
finalMessage = encryptDecrypt(cryptMode, startMessage)
print("Final message:", finalMessage)