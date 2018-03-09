from re import findall
alpha = tuple("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
cryptMode = input("[E]ncrypt|[D]ecrypt: ").upper()
if cryptMode not in ['E','D']:
    print("Error: mode is not Found!"); raise SystemExit
startMessage = input("Write the message: ").upper()
def regular(text):
    template = r"[0-9]+"
    return findall(template, text)
def encryptDecrypt(mode, message, final = ""):
    if mode == 'E': 
        for symbol in message:
            final += "%hu "%(alpha.index(symbol)+1)
    else: 
        for number in regular(message):
            final += "%c"%alpha[int(number)-1]
    return final
print("Final message:", encryptDecrypt(cryptMode, startMessage))
