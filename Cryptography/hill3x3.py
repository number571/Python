from re import findall

alpha = tuple("ABCDEFGHIJKLMNOPQRSTUVWXYZ ,.")
MatrixLength = 3; MatrixMod = len(alpha)

# Проверка условий на ошибки
def checkErrors(key):
    if len(key) != 9: return "Error: len(key) != 9"
    elif not getDeter(sliceto(key)): return "Error: det(Key) = 0"
    elif not getDeter(sliceto(key)) % MatrixMod: return "Error: det(Key) mod len(alpha) = 0"
    else: return None

# Регулярное выражение - 3 символа сообщения
def regular(text): 
    template = r".{3}"
    return findall(template, text)

# Кодирование символов в матрице
def encode(matrix): 
    for x in range(len(matrix)):
        for y in range(MatrixLength):
            matrix[x][y] = alpha.index(matrix[x][y])
    return matrix

# Декодирование чисел в матрице + шифрование/расшифрование
def decode(matrixM, matrixK, message = ""):
    matrixF = []
    for z in range(len(matrixM)):
        temp = [0,0,0]
        for x in range(MatrixLength):
            for y in range(MatrixLength):
                temp[x] += matrixK[x][y] * matrixM[z][y]
            temp[x] = alpha[temp[x] % MatrixMod]
        matrixF.append(temp)
    for string in matrixF: message += "".join(string)
    return message

# Создаёт матрицу по три символа
def sliceto(text): 
    matrix = []
    for three in regular(text): matrix.append(list(three))
    return encode(matrix)

# Нахождение обратного определителя матрицы
def iDet(det):
    for num in range(MatrixMod):
        if num * det % MatrixMod == 1:
            return num

# Алгебраические дополнения
def algebratic(x, y, det): 
    matrix = sliceto(mainKey)
    matrix.remove(matrix[x])
    for z in range(2):
        matrix[z].remove(matrix[z][y])
    iM = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    return (pow(-1, x + y) * iM * iDet(det)) % MatrixMod

# Получение определителя матрицы
def getDeter(matrix):
    return \
    (matrix[0][0] * matrix[1][1] * matrix[2][2]) + \
    (matrix[0][1] * matrix[1][2] * matrix[2][0]) + \
    (matrix[1][0] * matrix[2][1] * matrix[0][2]) - \
    (matrix[0][2] * matrix[1][1] * matrix[2][0]) - \
    (matrix[0][1] * matrix[1][0] * matrix[2][2]) - \
    (matrix[1][2] * matrix[2][1] * matrix[0][0])

# Получение алгебраических дополнений
def getAlgbr(det):
    algbrs = [0 for _ in range(9)]; index = 0
    for string in range(3):
        for column in range(3):
            algbrs[index] = algebratic(string, column, det); index += 1
    return algbrs

# Получение обратной матрицы
def getIMatr(algbr):
    return [
        [algbr[0],algbr[3],algbr[6]],
        [algbr[1],algbr[4],algbr[7]],
        [algbr[2],algbr[5],algbr[8]]
    ]

cryptMode = input("[E]ncrypt|[D]ecrypt: ").upper()
if cryptMode not in ['E','D']:
    print("Error: mode is not Found"); raise SystemExit
    
startMessage = input("Write the message: ").upper()
mainKey = input("Write the key: ").upper()

if checkErrors(mainKey): 
    print(checkErrors(mainKey)); raise SystemExit

for symbol in startMessage:
    if symbol not in alpha:
        startMessage = startMessage.replace(symbol,'')
        
while len(startMessage) % MatrixLength != 0: startMessage += startMessage[-1]

# Основная функция
def encryptDecrypt(mode, message, key):
    MatrixMessage, MatrixKey = sliceto(message), sliceto(key)
    if mode == 'E':
        final = decode(MatrixMessage, MatrixKey)
    else:
        algbr = getAlgbr(getDeter(MatrixKey))
        final = decode(MatrixMessage, getIMatr(algbr))
    return final
print("Final message:", encryptDecrypt(cryptMode, startMessage, mainKey))
