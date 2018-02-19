from re import findall

matrixLength = 2
MatrixKey = [[9,49],[2,11]]
det = MatrixKey[0][0]*MatrixKey[1][1] - MatrixKey[0][1]*MatrixKey[1][0]
if det != 1:
    print("Error: determinant != 1"); raise SystemExit
iMatrixKey = [
    [MatrixKey[1][1],-MatrixKey[0][1]],
    [-MatrixKey[1][0],MatrixKey[0][0]]]

alpha = tuple("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

cryptMode = input("[E]ncrypt|[D]ecrypt: ").upper()
if cryptMode not in ['E','D']:
    print("Error: mode is not Found!"); raise SystemExit

startMessage = input("Write the message: ").upper()
for symbol in startMessage:
    if symbol not in [chr(x) for x in range(65,91)]:
        startMessage = startMessage.replace(symbol,'')

while len(startMessage) % matrixLength != 0: startMessage += 'Z'

def regular(text):
    template = r"[A-Z]{"+str(matrixLength)+"}"
    return findall(template, text)

def encryptDecrypt(message, matrix, summ = 0, final = ""):
    for double in range(len(message)):
        for string in range(matrixLength):
            for column in range(matrixLength):
                summ += matrix[string][column] * alpha.index(message[double][column])
            final += alpha[(summ)%26]; summ = 0
    return final

if cryptMode == 'E': finalMessage = encryptDecrypt(regular(startMessage), MatrixKey)
else: finalMessage = encryptDecrypt(regular(startMessage), iMatrixKey)

print("Final message:",finalMessage)