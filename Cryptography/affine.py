mod = 26
print(end = "Key[a] possible: ")
for key in range(mod):
    if (pow(int(key),2)*int(key))%mod == 1:
        print(key, end = " ")
print()
cryptMode = input("[E]ncrypt|[D]ecrypt: ").upper()
if cryptMode not in ['E','D']:
    print("Error: mode is not Found!"); raise SystemExit
startMessage = input("Write the message: ").upper()
try: mainKey = input("Write the keys: ").split()
except ValueError: 
    print("Only int numbers!"); raise SystemExit
if len(mainKey) != 2:
    print("Error: qualitity keys must be 2"); raise SystemExit
if (pow(int(mainKey[0]),2)*int(mainKey[0]))%mod != 1: 
    print("Error: a^-1 * a != 1"); raise SystemExit
def encryptDecrypt(mode, message, key, final = ""):
    for symbol in message:
            if mode == 'E': 
                final += chr((int(key[0]) * ord(symbol) + int(key[1]) - 13)%mod + ord('A'))
            else: 
                final += chr(pow(int(key[0]),2) * ((ord(symbol) + mod - int(key[1]) - 13))%mod + ord('A'))
    return final
print("Final message:",encryptDecrypt(cryptMode, startMessage, mainKey))