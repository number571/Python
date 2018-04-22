# Вычисление простых чисел #
array = []
flag = False
for s in range(50,125):
	for i in range(2,s):
		if s % i == 0:
			flag = True
			break
	if flag == False:
		array.append(s)
	flag = False
array.append("...")
print("s:",array,'\n')

# Простые числа
p = 83; q = 113 # p = 3557; q = 2579
print("p = %d; q = %d"%(p,q))

n = p * q # Произведение
Fn = (p-1)*(q-1) # Функция Эйлера

print("n = %d; f(n) = %d\n"%(n, Fn))

# Подбор открытой экспоненты #
array = []
for e in range(1,25):
	d = int((1 + 2 * Fn) / e)
	if d * e == 1 + 2 * Fn:
		array.append(e)
array.append("...")
print("e:",array)

# Открытая экспонента
e = 3 # Простое число && e < n
print("e =", e,'\n')

# Подбор натурального числа k #
array = []
for k in range(1,25):
	d = int((1 + k * Fn) / e)
	if d * e == 1 + k * Fn:
		array.append(k)
array.append("...")
print("k:",array)

# Секретная экспонента
k = 2 # Натуральное число
d = int((1 + k * Fn) / e)

print("k = %d; d = %d\n"%(k,d))

# Условие на вычисление секретной экспоненты
if d * e != 1 + k * Fn:
	raise SystemExit

public_key = [e, n] # Публичный ключ
private_key = [d, n] # Приватный ключ

print("public_key:",public_key)
print("private_key:",private_key,'\n')

#'''
# Сообщение
m = 111
print("m =", m)

# Шифрование
Cm = m ** e % n
print("Cm =", Cm)

# Расшифрование
Dm = Cm ** d % n
print("Dm =", Dm)
#'''

'''
dictCodes = {chr(value+55):value for value in range(10,36)}

message = "Hello World".upper()
for symbol in message:
	if symbol not in [chr(x) for x in range(65, 91)]:
		message = message.replace(symbol,'')
print("message =", message)

codes = []
for symbol in message:
	codes.append(dictCodes[symbol])
print("codes =", codes,'\n')

# Шифрование
encrypt = []
for m in codes:
	encrypt.append(m ** e % n)
print("encrypt =", encrypt)

# Расшифрование
codes = []
for c in encrypt:
	codes.append(int(c) ** d % n)
decrypt = ""
for code in codes:
	for key in dictCodes:
		if code == dictCodes[key]:
			decrypt += key
print("decrypt =", decrypt)
'''
