# Cipher created from: https://github.com/pravdakotchestno

m = 32; n = 127; length = n - m
dictN = {x-m+1 : chr(x) for x in range(m,n)}
dictC = {chr(x) : x-m+1 for x in range(m,n)}

cryptMode = input("[E]ncrypt|[D]ecrypt: ").upper()
if cryptMode not in ['E','D']:
    print("Error: mode is not found")
    raise SystemExit

startMessage = input("Write the message: ")
mainKey = int(input("Write the key: "))
for symbol in startMessage:
    if symbol not in [chr(x) for x in range(m,n)]:
        startMessage = startMessage.replace(symbol, '')

def encrypt(message, key, result = ""):
    for index, symbol in enumerate(message):
        pos = len(message) - index
        result += dictN[(dictC[symbol]+(pos*key)+key)%length+1]
        key = sumAll(message[:len(message)-pos+1])%(n-m)
    return result

def decrypt(message, key, result = ""):
    for index, symbol in enumerate(message):
        pos = len(message) - index
        result += dictN[(dictC[symbol]-(pos*key)-key-2)%length+1]
        key = sumAll(result)%(n-m)
    return result

def sumAll(message, summ = 0):
    for symbol in message: summ += dictC[symbol]
    return summ

def toString(listS, final = ""):
    for symbol in listS: final += symbol
    return final

def encryptDecrypt(mode, message, key):
    if mode == 'E':
        enc_message = list(encrypt(message, key))
        enc_message.reverse()
        return encrypt(toString(enc_message), key)
    else:
        dec_message = list(decrypt(message, key))
        dec_message.reverse()
        return decrypt(toString(dec_message), key)

print("Final message:", encryptDecrypt(cryptMode, startMessage, mainKey))
