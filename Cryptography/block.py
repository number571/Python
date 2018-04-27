from re import findall

BLOCK = 3

def regular(text): 
    template = r".{"+str(BLOCK)+"}"
    return findall(template, text)

mes, m = "helloworld", []
while len(mes) % BLOCK != 0: mes += '0'
for three in regular(mes): m.append(list(three))
print(m)

for block in range(len(m)):
	for cell in range(len(m[block])):
		m[block][cell] = ord(m[block][cell])
print(m,'\n')

key = list("j@4")
for cell in range(len(key)):
	key[cell] = ord(key[cell])
mainKey = key[0]
for index in range(1,BLOCK): mainKey ^= key[index]

vector = list("#fw")
for cell in range(len(vector)):
	vector[cell] = ord(vector[cell])
vecInit = vector[0]
for index in range(1,BLOCK): vecInit ^= vector[index]

e = []
for _ in range(len(mes)//BLOCK): e.append([])
for cell in range(len(m[0])):
	e[0].append(m[0][cell] ^ vecInit ^ mainKey)
for block in range(1,len(m)):
	vecInitAfter = e[block-1][0]
	for index in range(1, BLOCK): vecInitAfter ^= e[block-1][index]
	for cell in range(len(m[block])):
		e[block].append(m[block][cell] ^ vecInitAfter ^ mainKey)
print(e)

encrypt = []
for _ in range(len(mes)//BLOCK): encrypt.append([])
for block in range(len(e)):
	for cell in range(len(e[block])):
		encrypt[block].append(chr(e[block][cell]))
print(encrypt,'\n')

d = []
for _ in range(len(e)): d.append([])
for cell in range(len(e[0])):
	d[0].append(e[0][cell] ^ vecInit ^ mainKey)
for block in range(1,len(e)):
	vecInitAfter = e[block-1][0]
	for index in range(1, BLOCK): vecInitAfter ^= e[block-1][index]
	for cell in range(len(e[block])):
		d[block].append(e[block][cell] ^ vecInitAfter ^ mainKey)
print(d)

for block in range(len(d)):
	for cell in range(len(d[block])):
		d[block][cell] = chr(d[block][cell])
print(d)
