from re import findall

alpha = tuple("ABCDEFGHIJKLMNOPQRSTUVWXYZ .?")
MatrixLength = 3; MatrixMod = 26
mainKey = "GYBNQKURP"

if len(mainKey) % 9 != 0: 
    print("Error: len(key) % 9 != 0"); raise SystemExit

cryptMode = input("[E]ncrypt|[D]ecrypt: ").upper()
if cryptMode not in ['E','D']:
    print("Error: mode is not Found!"); raise SystemExit

startMessage = input("Write the message: ").upper()
for symbol in startMessage:
    if symbol not in alpha:
        startMessage = startMessage.replace(symbol,'')
while len(startMessage) % MatrixLength != 0: startMessage += 'Z'

def regular(text): 
    template = r"[A-Z]{3}"
    return findall(template, text)

def code(matrix): 
    for x in range(len(matrix)):
        for y in range(MatrixLength):
            matrix[x][y] = alpha.index(matrix[x][y])
    return matrix

def decode(matrixM, matrixK, message = "", matrixF = []):
    for z in range(len(matrixM)):
        temp = [0,0,0]
        for x in range(MatrixLength):
            for y in range(MatrixLength):
                temp[x] += matrixM[z][y] * matrixK[x][y]
            temp[x] = alpha[temp[x] % MatrixMod]
        matrixF.append(temp)
    for string in matrixF: message += "".join(string)
    return message

def sliceto(text): 
    matrix = []
    for three in regular(text): matrix.append(list(three))
    return code(matrix)

def algebratic(x, y, det): 
    matrix = sliceto(mainKey)
    matrix.remove(matrix[x])
    for z in range(2):
        matrix[z].remove(matrix[z][y])
    var = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    return (pow(-1, x + y) * var * det) % MatrixMod

def getDeter(matrix):
    det = \
        matrix[0][0] * matrix[1][1] * matrix[2][2] - \
        matrix[0][0] * matrix[1][2] * matrix[2][1] - \
        matrix[0][1] * matrix[1][0] * matrix[2][2] + \
        matrix[0][1] * matrix[1][2] * matrix[2][0] + \
        matrix[0][2] * matrix[1][0] * matrix[2][1] - \
        matrix[0][2] * matrix[1][1] * matrix[2][0]
    return det

def getAlgbr(det):
    iElems = [0 for _ in range(9)]; index = 0
    for string in range(3):
        for column in range(3):
            iElems[index] = algebratic(string, column, det); index += 1
    return iElems

def getIMatr(alg):
    iMatrixKey = [
        [alg[0],alg[3],alg[6]],
        [alg[1],alg[4],alg[7]],
        [alg[2],alg[5],alg[8]]
    ]
    return iMatrixKey

def encryptDecrypt(mode, message, key, final = "", matrixFinal = []):
    MatrixMessage, MatrixKey = sliceto(message), sliceto(key)
    if mode == 'E':
        final = decode(MatrixMessage, MatrixKey)
    else:
        deter = getDeter(MatrixKey); algbr = getAlgbr(deter)
        final = decode(MatrixMessage, getIMatr(algbr))
    return final
print("Final message:", encryptDecrypt(cryptMode, startMessage, mainKey))