print("Possible Key[a]: 1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25.")
cryptMode = input("[E]ncrypt|[D]ecrypt: ").upper()
if cryptMode not in ['E','D']:
    print("Error: mode is not Found!"); raise SystemExit
startMessage = input("Write the message: ").upper()
mainKey = input("Write the keys: ").split()
for key in mainKey:
	try: int(key)
	except: print("Only int numbers!"); raise SystemExit
if len(mainKey) != 2:
    print("Error: qualitity keys must be 2"); raise SystemExit
def encryptDecrypt(mode, message, key, final = ""):
    for symbol in message:
            if mode == 'E': 
                final += chr((int(key[0]) * ord(symbol) + int(key[1]) - 13)%26 + ord('A'))
            else: 
                final += chr(pow(int(key[0]),11) * ((ord(symbol) + 26 - int(key[1]) - 13))%26 + ord('A'))
    return final
print("Final message:",encryptDecrypt(cryptMode, startMessage, mainKey))
