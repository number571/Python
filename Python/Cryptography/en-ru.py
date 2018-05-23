alphaEn = tuple("QWERTYUIOP[]ASDFGHJKL;'ZXCVBNM,.~")
alphaRu = tuple("ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮЁ")
startMessage = input("Write the message: ").upper()
def encryptDecrypt(message, alpha, final = ""):
    for symbol in message:
        try: final += alpha[1][alpha[0].index(symbol)]
        except ValueError: final += alpha[0][alpha[1].index(symbol)]
    return final
print("Final message:", encryptDecrypt(startMessage, [alphaEn, alphaRu]))
