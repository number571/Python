from random import randint
from re import findall
cryptMode = input("[E]ncrypt|[D]ecrypt: ").upper()
if cryptMode not in ['E','D']:
    print("Error: mode is not found")
    raise SystemExit
startMessage = input("Write the message: ")
def regular(text):
    return findall(r"[0-9]+", text)
def encryptDecrypt(mode, message, final = [], keys = []):
    if mode == 'E':
        for symbol in message:
            key = randint(0,25); keys.append(str(key))
            final.append(str(ord(symbol) ^ key))
        return '.'.join(final), '.'.join(keys)
    else: 
        keys = input("Write the keys: ")
        for index, symbol in enumerate(regular(message)):
            final.append(chr(int(symbol) ^ int(regular(keys)[index])))
        return ''.join(final)
print("Final message:",encryptDecrypt(cryptMode, startMessage))
