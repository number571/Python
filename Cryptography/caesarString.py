cryptMode = input("[E]ncrypt|[D]ecrypt: ").upper()
if cryptMode not in ['E','D']:
    print("Error: mode is not Found!"); raise SystemExit
    
alphaList = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
startMessage = input("Write the message: ").upper()

for symbol in startMessage:
    if symbol not in alphaList:
        startMessage = startMessage.replace(symbol,"")

try: numberKey = int(input("Write the number key: "))
except ValueError: print("Error: only int number!"); raise SystemExit
    
stringKey = list(input("Write the string key: ").upper())

def remove(alpha, string):
    for symbol in string:
        if symbol in alpha: alpha.remove(symbol)
    for symbol in string:
        if symbol not in [chr(x) for x in range(65,91)] \
        or string.count(symbol) > 1: string.remove(symbol) 
    return alpha, string

def insert(alpha_string):
    for index, symbol in enumerate(alpha_string[1]):
        alpha_string[0].insert(index, symbol)
    return alpha_string[0]

def replace(alpha, key):
    while key > 0:
        alpha.insert(0,alpha[-1])
        del alpha[-1]
        key -= 1
    return alpha

def encryptDecrypt(mode, message, key, final = ""):
    alphaS = [x for x in alphaList]
    alphaC = replace(insert(remove(alphaList, stringKey)),key)
    for symbol in message:
        if mode == 'E':
            final += alphaC[alphaS.index(symbol)]
        else: 
            final += alphaS[alphaC.index(symbol)]
    return final
print("Final message:", encryptDecrypt(cryptMode, startMessage, numberKey))
