cryptMode = input("[E]ncrypt|[D]ecrypt: ").upper()
if cryptMode not in ['E','D']:
    print("Error: mode is not Found!"); raise SystemExit
startMessage = input("Write the message: ").upper()
try:numberKey = int(input("Write the number key: "))
except ValueError: print("Only numbers!"); raise SystemExit
alpha = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
stringKey = list(input("Write the string key: ").upper())
for symbol in stringKey:
    if symbol not in [chr(x) for x in range(65,91)] \
    or stringKey.count(symbol) > 1: stringKey.remove(symbol)
    if symbol in alpha: alpha.remove(symbol)
for index, symbol in enumerate(stringKey):
    alpha.insert((numberKey+index)%26, symbol)
print(alpha)
def encryptDecrypt(mode, message, key, final = ""):
    for symbol in message:
        if mode == 'E':
            final += alpha[(alpha.index(symbol) + key)%26]
        else: 
            final += alpha[(alpha.index(symbol) - key)%26]
    return final
print("Final message:", encryptDecrypt(cryptMode, startMessage, numberKey))
