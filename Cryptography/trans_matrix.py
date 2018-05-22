from random import randint

message = input("Write the message: ")
length = len(message)

try: matrixLength = int(input("Matrix length: "))
except ValueError: 
    print("Error: only int number")
    raise SystemExit
matrixSquare = matrixLength ** 2

divF = length / matrixSquare
divI = length // matrixSquare
QUAN = divI if divF <= divI else divI + 1

def sliceMessage(message, index = 0, slices = []):
    for _ in range(QUAN):
        slices.append(message[index:index+matrixSquare])
        index += matrixSquare
    return slices

def appendSymbol(slices):
    while len(slices[-1]) % matrixSquare != 0:
        slices[-1] += chr(randint(65,90))
    return slices

def getMatrix(slices):
    for matrix in range(QUAN):
        text, slices[matrix], index = slices[matrix], [], 0
        for _ in range(matrixLength):
            slices[matrix].append(list(text[index:index+matrixLength]))
            index += matrixLength
    return slices

def getTransMatrix(matrixes):
    trans_matrix = []
    for matrix in range(QUAN):
        temp_matrix = []
        for _ in range(matrixLength):
            temp_matrix.append([0 for _ in range(matrixLength)])
        for string in range(matrixLength):
            for column in range(matrixLength):
                temp_matrix[string][column] = matrixes[matrix][column][string]
        trans_matrix.append(temp_matrix)
    return trans_matrix

def matrixMessage(matrixes, final = ""):
    for matrix in range(QUAN):
        for string in range(matrixLength):
            for column in range(matrixLength):
                final += matrixes[matrix][string][column]
    return final

matrix = getMatrix(appendSymbol(sliceMessage(message)))
encrypt = matrixMessage(getTransMatrix(matrix))
print("Final message:", encrypt)
