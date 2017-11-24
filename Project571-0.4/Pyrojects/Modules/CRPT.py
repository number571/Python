from Modules import HEAD, TERM
def choose():
	crpt="" # Создаём нулевую переменную
	while crpt not in TERM.Command_ADDT["Back"]: # Пока переменная не равняется нулю делать следующее:
		crpt=input("[root@"+TERM.Hostname+" crpt]# ")
		if   crpt in TERM.Command_CRPT["Caesar"]: caesar() # Если переменная равна единице: Вывести шифр Цезаря
		elif crpt in TERM.Command_CRPT["Vishener"]: vishener() # Если переменная равна двойке: Вывести шифр Виженера
		elif crpt in TERM.Command_CRPT["Replace"]: replace() # Если переменная равна тройке: Вывести шифр замены
		elif crpt in TERM.Command_CRPT["Homophonic"]: homophonic() # Если переменная равна четвёрке: Вывести омофонический шифр
		elif crpt in TERM.Command_CRPT["RSA"]: rsa()  # Если переменная равна пятёрке: Вывести шифр RSA
		elif crpt in TERM.Command_CRPT["AES"]: aes()  # Если переменная равна шестёрке: Вывести шифр AES
		elif crpt in TERM.Command_CRPT["XOR"]: xor()  # Если переменная равна семёрке: Вывести шифр XOR
		elif crpt in TERM.Command_CRPT["Cryptanalysis"]: cryptanalysis() # Если переменная равна нулю: Вывести криптоанализ
		elif crpt in TERM.Command_ADDT["Check"]: title() # При вызове ls Получим титульную часть выбора
		elif crpt in TERM.Command_ADDT["Help"]: HEAD.help() # При вызове help Получим краткий мануал команд
		elif crpt in TERM.Command_ADDT["Info"]: HEAD.info() # Дополнительная информация
		elif crpt in TERM.Command_ADDT["Clear"]: HEAD.clear() # При вызове clear Очистится история программы
		elif crpt in TERM.Command_ADDT["Back"]: continue # Происходит возврат на один пункт назад
		elif crpt in TERM.Command_ADDT["Exit"]: raise SystemExit # Выход из программы
		else: print("?:",crpt,":command not found") # Если не найдены вышеперечисленные значения

def title(): # Титульная часть выбора метода шифрования
	print(HEAD.Line["full-"]+"\n[>] Write the number:")
	print("\t1) CAESAR.571\n\t2) VISHENER.571\n\t3) REPLACE.571\n\t4) HOMOPHONIC.571\n\t5) RSA.571\n\t6) AES.571\n\t7) XOR.571")
	print(HEAD.Line["nfull-"]+"\n\t0) CRYPTANALYSIS.571\n"+HEAD.Line["full-"])

def xor():
	print(HEAD.Line["full-"]+"\n"+HEAD.Line["crpt"]+"\n"+HEAD.Line["full-"])
	print("1) Crypt the message\n2) Decrypt the message\n"+HEAD.Line["full-"])
	answer = input("[*] Write the number: ")
	print(HEAD.Line["full-"])
	if answer == "1":
		text = input("\tWrite the text: ")
		key = input("\tWrite the key: ")
		crypt = ""
		for i in text:
				try:
					crypt += chr(ord(i)^int(key))
				except:
					crypt += chr(ord(i)^ord(key))
		print(HEAD.Line["full-"]+"\n[+] Crypted message: "+crypt+"\n"+HEAD.Line["full-"])
	elif answer == "2":
		crypt = input("\tWrite the crypt-text: ")
		key = input("\tWrite the key: ")
		decrypt = ""
		for j in crypt:
				try:
					decrypt += chr(ord(j)^int(key))
				except:
					decrypt += chr(ord(j)^ord(key))
		print(HEAD.Line["full-"]+"\n[+] Decrypted message: "+decrypt+"\n"+HEAD.Line["full-"])
	else:
		print(HEAD.Line["full-"]+"\n[x] Number is not found!\n"+HEAD.Line["full-"])

def cryptanalysis():
	print(HEAD.Line["full-"]+"\n"+HEAD.Line["crpt"]+"\n"+HEAD.Line["full-"])
	print('''
\t\t A = 8.17% \t N = 6.75% 
\t\t B = 1.49% \t O = 7.51%  
\t\t C = 2.78% \t P = 1.93%
\t\t D = 4.25% \t Q = 0.10%
\t\t E = 12.7% \t R = 5.99%
\t\t F = 2.23% \t S = 6.33%
\t\t G = 2.02% \t T = 9.06% 
\t\t H = 6.09% \t U = 2.76%
\t\t I = 6.97% \t V = 0.98%
\t\t J = 0.15% \t W = 2.36% 
\t\t K = 0.77% \t X = 0.15%
\t\t L = 4.03% \t Y = 1.97%
\t\t M = 2.41% \t Z = 0.05%
'''+HEAD.Line["full="]) # Информация о частоте встречаемости английских символов
	name = input("File-name: ") # Имя файла
	print(HEAD.Line["full-"]); text = "" # Объявление переменной текст
	try: # Проверка на наличие ошибки поиска файла
		with open(name,"r") as file: # Открыть файл в режиме чтения
			original = file.read() # Считать весь текст в переменную original
	except FileNotFoundError: # Если ошибка
		print("File is not found!") # Вывести сообщение
	else: # Иначе если всё прошло успешно
		for i in original: # Посимвольный перебор оригинального текста
			if i !=" ": # Если символ не равен пробелу, то добавить символ в переменную text
				text += i 
			else: # Иначе пропустить
				pass 
	dict = {i for i in text} # Создание множества не повторяющихся символов
	def check(words, char): # Объявление функции, которая принимает тект и символ
		k = 0 # Объявление переменной - счётчика
		for i in words: # Посимвольный перебор текста
			if i == char: # Если символ переменная i = символу, то к счётчику прибавить единицу
				k += 1 
		return k # Возврат счётчика k
	percent = 100 # 100 процентов
	length = len(text) # Длина текста без пробелов
	var = 0 # Объявление счётчика
	print("[*] Result: ")
	for symbol in dict: # Посимвольный перебор множества
		stat = percent * check(text,symbol) / length # Занести процентное соотношение частоты символа в переменную stat
		if var%2 == 0: # Если var чётная переменная, вывести это сообщение:
			print("\t\t{0} - {1}%\t".format(symbol,round(stat,2)),end=""); var += 1 # К var прибавить единицу
		else: # Иначе выводить другое сообщение:
			print("{0} - {1}%".format(symbol,round(stat,2))); var += 1 # К var прибавить единицу
	if var%2 == 0: 
		print(HEAD.Line["full-"])
	else: 
		print("\n"+HEAD.Line["full-"])

def replace(): # Шифр замены
	from random import choice
	print(HEAD.Line["full-"]+"\n"+HEAD.Line["crpt"]+"\n"+HEAD.Line["full-"])
	arr1=['!','@','#','$','%','^','&','*','(',')','-','=','+','?',':',';','<','>','/','[',']','{','}','|','.',',','~']
	arr=[] # Все возможные символы замены
	for i in range(len(arr1)): # Рандомное распределение символов
		n=choice(arr1) 
		arr1.remove(n) 
		arr.append(n) 
	puts='''
keys={
	'A':"'''+arr[0]+'''",  'B':"'''+arr[1]+'''",  'C':"'''+arr[2]+'''",
	'D':"'''+arr[3]+'''",  'E':"'''+arr[4]+'''",  'F':"'''+arr[5]+'''",
	'G':"'''+arr[6]+'''",  'H':"'''+arr[7]+'''",  'I':"'''+arr[8]+'''",
	'J':"'''+arr[9]+'''",  'K':"'''+arr[10]+'''",  'L':"'''+arr[11]+'''",
	'M':"'''+arr[12]+'''",  'N':"'''+arr[13]+'''",  'O':"'''+arr[14]+'''",
	'P':"'''+arr[15]+'''",  'Q':"'''+arr[16]+'''",  'R':"'''+arr[17]+'''",
	'S':"'''+arr[18]+'''",  'T':"'''+arr[19]+'''",  'U':"'''+arr[20]+'''",
	'V':"'''+arr[21]+'''",  'W':"'''+arr[22]+'''",  'X':"'''+arr[23]+'''",
	'Y':"'''+arr[24]+'''",  'Z':"'''+arr[25]+'''",  ' ':"'''+arr[26]+'''"}
'''
	with open("crypt.py","w") as crypt: 
		crypt.write('''
text1=input("Write the text: "); text="" # Открытый текст
for i in text1: # Посимвольное чтение текста
	if i.islower(): text+=i.upper() # Если текст с малого регистра - перевести его в большой регистр и добавить к переменной текст символ
	else: text+=i # Иначе добавить к переменной текст символ
crypt="" # Объявление переменной для занесения зашифрованного сообщения
'''+puts+''' # Ключи
for i in text: # Посимвольный перебор открыторого сообщения с большим регистром
	if i in keys: # Если символ находится в ключе
		crypt+=keys[i] # Добавить его второй параметр
	else: pass # Иначе пропуск
print("Crypted text: "+crypt) # Вывести зашифрованное сообщение
''')
		print("[+] File 'crypt.py' successfully saved!")
	with open("key.py","w") as key: 
		key.write('''
crypt=input("Write the crypt-text: "); decrypt="" # Зашифрованный текст
'''+puts+''' # Ключи
for i in crypt: # Посимвольное чтение зашифрованного сообщения
	for j in keys: # Посимвольное чтение ключей
		if i in keys[j]: decrypt+=j Если символ i находится под ключом j, то добавить j
		else: pass # Иначе пропуск
print("Decrypted text: "+decrypt)''')
		print("[+] File 'key.py' successfully saved!\n"+HEAD.Line["full-"])

def homophonic(): # Омофонический шифр
			from random import choice
			print(HEAD.Line["full-"]+"\n"+HEAD.Line["crpt"]+"\n"+HEAD.Line["full-"])
			arr1=['1','2','3','4','5','6','7','8','9','0','a','b','c',\
			'd','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s',\
			't','u','v','w','x','y','z','!','@',' ','#','№','$',';','%','^',\
			':','&','?','(',')','-','_','+','=','`','~','[',']','{',\
			'}','.',',','/','|','A','B','C','D','E','F','G','H','J','K','L',\
			'M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','<',\
			'>','А','М','В','С','у','Е','Т','а','Х','З','х','О','e','о'] # Все возможные символы замены
			arr=[] 
			for i in range(len(arr1)): # Рандомное распределение символов
				n=choice(arr1)
				arr1.remove(n)
				arr.append(n) 
			puts='''
keys={
	'A':["'''+arr[0]+'''","'''+arr[1]+'''","'''+arr[2]+'''","'''+arr[3]+'''","'''+arr[4]+'''","'''+arr[5]+'''","'''+arr[6]+'''","'''+arr[7]+'''"],
	'B':["'''+arr[8]+'''","'''+arr[9]+'''"],
	'C':["'''+arr[10]+'''","'''+arr[11]+'''","'''+arr[12]+'''"],
	'D':["'''+arr[13]+'''","'''+arr[14]+'''","'''+arr[15]+'''","'''+arr[16]+'''"],
	'E':["'''+arr[17]+'''","'''+arr[18]+'''","'''+arr[19]+'''","'''+arr[20]+'''","'''+arr[21]+'''","'''+arr[22]+'''","'''+arr[23]+'''","'''+arr[24]+'''","'''+arr[25]+'''","'''+arr[26]+'''","'''+arr[27]+'''","'''+arr[28]+'''"],
	'F':["'''+arr[29]+'''","'''+arr[30]+'''"],
	'G':["'''+arr[31]+'''","'''+arr[32]+'''"],
	'H':["'''+arr[33]+'''","'''+arr[34]+'''","'''+arr[35]+'''","'''+arr[36]+'''","'''+arr[37]+'''","'''+arr[38]+'''"],
	'I':["'''+arr[39]+'''","'''+arr[40]+'''","'''+arr[41]+'''","'''+arr[42]+'''","'''+arr[43]+'''","'''+arr[44]+'''"],
	'J':["'''+arr[45]+'''"],
	'K':["'''+arr[46]+'''"],
	'L':["'''+arr[47]+'''","'''+arr[48]+'''","'''+arr[49]+'''","'''+arr[50]+'''"],
	'M':["'''+arr[51]+'''","'''+arr[52]+'''"],
	'N':["'''+arr[53]+'''","'''+arr[54]+'''","'''+arr[55]+'''","'''+arr[56]+'''","'''+arr[57]+'''","'''+arr[58]+'''"],
	'O':["'''+arr[59]+'''","'''+arr[60]+'''","'''+arr[61]+'''","'''+arr[62]+'''","'''+arr[63]+'''","'''+arr[64]+'''","'''+arr[65]+'''"],
	'P':["'''+arr[66]+'''","'''+arr[67]+'''"],
	'Q':["'''+arr[68]+'''"],
	'R':["'''+arr[69]+'''","'''+arr[70]+'''","'''+arr[71]+'''","'''+arr[72]+'''","'''+arr[73]+'''","'''+arr[74]+'''"],
	'S':["'''+arr[75]+'''","'''+arr[76]+'''","'''+arr[77]+'''","'''+arr[78]+'''","'''+arr[79]+'''","'''+arr[80]+'''"],
	'T':["'''+arr[81]+'''","'''+arr[82]+'''","'''+arr[83]+'''","'''+arr[84]+'''","'''+arr[85]+'''","'''+arr[86]+'''","'''+arr[87]+'''","'''+arr[88]+'''","'''+arr[89]+'''"],
	'U':["'''+arr[90]+'''","'''+arr[91]+'''","'''+arr[92]+'''"],
	'V':["'''+arr[93]+'''"],
	'W':["'''+arr[94]+'''","'''+arr[95]+'''"],
	'X':["'''+arr[96]+'''"],
	'Y':["'''+arr[97]+'''","'''+arr[98]+'''"],
	'Z':["'''+arr[99]+'''"],
	' ':["'''+arr[100]+'''","'''+arr[101]+'''","'''+arr[102]+'''","'''+arr[103]+'''","'''+arr[104]+'''"] }'''
			with open("crypt.py","w") as crypt: 
				crypt.write('''
from random import randint
'''+puts+''' # Ключи
text1=input("Write the text: "); text="" # Открытый текст
for i in text1: # Посимвольный перебор открытого сообщения
	if i.islower(): text+=i.upper() # Если символ имеет малый регистр - заменить его на большой регистр и добавить символ к переменной
	else: text+=i # Иначе добавить просто символ
crypt="" # Объявление переменной для хранения зашифрованного сообщения
for i in text: # Посимвольный перебор открытого сообщения с большим регистром
	if i in keys: lenght=len(keys[i]); crypt+=keys[i][randint(0,lenght-1)] # Если символ находится в ключах - выбрать рандомный ключ для данного символа 
print(crypt) # Вывести зашифрованное сообщение
''') 
				print("[+] File 'crypt.py' successfully saved!")
			with open("key.py","w") as key: 
				key.write('''
'''+puts+''' # Ключи
crypt=input("Write the crypted-text: "); decrypt="" # Зашифрованное сообщение и объявление переменной для хранения расшифрованного текста
for i in crypt: # Посимвольный перебор зашифрованного сообщения
	for j in keys: # Перебор ключей
		if i in keys[j]: decrypt+=j # Если символ i находится в ключе j, то добавить j
		else: pass # Иначе пропуск 
print(decrypt)''') 
				print("[+] File 'key.py' successfully saved!\n"+HEAD.Line["full-"])

def caesar(): # Шифр Цезаря
			arr1=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
			arr2=list(map(lambda x:x,arr1)) # Создаём новый массив
			def change_arr2(number): # Замена символов при помощи ключа 'number'
				for i in range(number): # Происходит перебор символов
					arr2.append(arr2[0]) # Сначала добавляется нулевой индекс в конец списка
					arr2.remove(arr2[0]) # Далее этот же нулевой индекс удаляется
			def create_decrypt(decrypt):
				number=int(input("[*] Write the key-number [0-%s]: "%(str(len(arr1))))) # Выводит количество символов в массиве
				change_arr2(number) # Происходит перебор символов
				if decrypt=="with_file":
					with open("text_crypt.txt","r") as decrypt_r: # Чтение файла
						msg=decrypt_r.read() 
				elif decrypt=="without_file": # Пишем зашифрованное сообщение
					msg=input("[*] Write the crypted text: ") 
				else: 
					raise SystemExit
				msgd="" # Создаём новую нулевую переменную
				for i in msg: # Перебор символов из зашифрованного сообщения
					if i==" ": # Добавление пробелов
						msgd+=" " 
					else:
						for j in range(len(arr1)): # Просмотр длины массива
							if i==arr2[j]: # При совпадении символов из сообщения с вторым массивом происходит замена на символ первого массива
								msgd+=arr1[j] 
				print(HEAD.Line["full-"]+"\n[!] Decrypted text: "+str(msgd)+"\n"+HEAD.Line["full-"]) # Вывод расшифрованного сообщения
			print(HEAD.Line["full-"]+"\n"+HEAD.Line["crpt"]+"\n"+HEAD.Line["full-"])
			print("1) Crypt the text/file\n2) Decrypt text from the file\n3) Decrypt text from the terminal")
			try: # Ошибка в случае напичания не целого числа
				ans=int(input(HEAD.Line["full-"]+"\n[*] Write the number:\n[number] > ")) # Выбор действия
				if ans==1: # Шифрование сообщения
					num=int(input("[*] Write the key-number [0-%s]: "%(str(len(arr1))))) # Выводит количество символов в массиве
					change_arr2(num)
					msg1=input("[*] Write the text: ") # Пишем наше сообщение
					msg="" 
					for i in msg1: # Если символ с малого регистра- заменить его на большой
						if i.islower(): 
							msg+=i.upper()
						else: 
							msg+=i
					msgc="" # Создаём новую нулевую переменную
					for i in msg: # Перебор символов из сообщения
						if i==" ": # Добавление пробелов
							msgc+=" " 
						else:
							for j in range(len(arr1)): # Просмотр длины массива
								if i==arr1[j]: # При совпадении символов из сообщения с первым массивом происходит замена на символ второго массива
									msgc+=arr2[j] 
					with open("text_crypt.txt","w") as crypt: # Создание файла
						print(HEAD.Line["full-"]+"\n[!] Crypted-text: "+msgc)
						crypt.write(msgc) # Сохранение зашифрованного сообщения в файл
						print("[+] File 'text_crypt.txt' successfully saved!\n"+HEAD.Line["full-"])
				elif ans==2: 
					create_decrypt("with_file") # Расшифровка сообщения из файла
				elif ans==3: 
					create_decrypt("without_file") # Расшифровка сообщения из терминала
				else: 
					print("Number is not defined!") # Если ввели число не в интервале 1-3
			except ValueError: 
				print("Error! Print only Integer numbers!") # Если ввели вместо целого числа иные символы

def rsa(): # Шифр RSA
			import rsa
			(pub,priv)=rsa.newkeys(1024) # Генерация открытого и закрытого ключей
			print(HEAD.Line["full-"]+"\n"+HEAD.Line["crpt"]+"\n"+HEAD.Line["full-"])
			print("\n"+str(pub)+"\n\n"+str(priv)+"\n") # Вывод открытого и закрытого ключей
			with open("crypt.py","w") as crypt: 
				crypt.write('''
import rsa 
pub_key=int(input("Write the PublicKey: ")) # Способ шифрования при помощи открытого ключа
text=input("\\n[*] Write the text:\\n\\n[text] >> ") # Ввод открытого сообщения
message=text.encode("utf8") # Преобразование в юникод
crypt=rsa.encrypt(message,rsa.PublicKey(pub_key,65537)) # Шифрование сообщения
with open("text_crypt.txt","wb") as w: # Создание файла
	w.write(crypt) # Запись в файл зашифрованного сообщения
	print("\\n[*] Crypt-text:\\n\\n"+str(crypt)+"\\n\\n[+] File: 'text_crypt.txt' successfully saved!\\n")
''')
				print("\n[+] File: 'crypt.py' successfully saved!") 
			with open("key.py","w") as key: 
				key.write('''
import rsa
file=input("Write the filename: ") # Указать зашифрованный файл
with open(file,"rb") as r: # Открыть данный файл
	read=r.read() # Прочитать файл
	message=rsa.decrypt(read,rsa.'''+str(priv)+''') # Расшифровать сообщение в файле
	print("\\n[*] Decrypted text:\\n\\n[text] << "+str(message.decode("utf8"))+"\\n")
''') 
				print("[+] File: 'key.py' successfully saved!\n")

def aes(): # Функция AES шифрования
			print(HEAD.Line["full-"]+"\n"+HEAD.Line["crpt"]+"\n"+HEAD.Line["full-"])
			with open("crypt.py","w") as crypt: 
				crypt.write('''
import pyAesCrypt
print("'''+HEAD.Line["full-"]+'''")
file=input("File name: ") # Ввод имени файла
password=input("Password: ") # Ввод пароля для файла
bufferSize = 512*1024 # Указываем размер буфера (чем больше файл, тем больше ставьте размер буфера) 
try: pyAesCrypt.encryptFile(str(file), str(file)+".crp", password, bufferSize) # Шифрование файла
except FileNotFoundError: print("[x] File not found!") # Если ошибка - вывести сообщение, что файл не найден
else: print("[+] File '"+str(file)+".crp' successfully saved!") # Иначе если всё успешно - вывести сообщения сохранения зашифрованного файла
finally: print("'''+HEAD.Line["full-"]+'''")''') 
				print(HEAD.Line["full-"]+"\n[+] File: 'crypt.py' successfully saved!") # Вывод сообщения, если всё прошло удачно
			with open("key.py","w") as key: 
				key.write('''
import pyAesCrypt
print("'''+HEAD.Line["full-"]+'''")
file=input("File name: ") # Ввод имени файла
password=input("Password: ") # Ввод пароля для файла
bufferSize = 512*1024 # Указываем размер буфера (чем больше файл, тем больше ставьте размер буфера)
try: pyAesCrypt.decryptFile(str(file), str(os.path.splitext(file)[0]), password, bufferSize) # Расшифрование файла 
except FileNotFoundError: print("[x] File not found!") # Если ошибка файла - вывести сообщение, что файл не найден
except ValueError: print("[x] Password is False!") # Если ошибка пароля - вывести сообщение, что пароль неверный
else: print("[+] File '"+str(os.path.splitext(file)[0])+"' successfully saved!") # Иначе если всё успешно - вывести сообщения сохранения расашифрованного файла
finally: print("'''+HEAD.Line["full-"]+'''")'''); 
				print("[+] File: 'key.py' successfully saved!\n"+HEAD.Line["full-"]) # Вывод сообщения, если всё прошло удачно

def vishener(): # Шифр Виженера
			arr=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
			print() # Схематическое изображение квадрата Виженера #
			def switch(n):
				while n<26: # От 0 до 26 (Английский алфавит) #
					for i in arr:
						if i==arr[0]:
							print(end="|") # Начало строки с '|' #
						print(i,end="|") # 26 символов в одну строку #
					arr.append(arr[0]) # Добавление нулевого индекса в конец массива #
					arr.remove(arr[0]) # Удаление нулевого индекса #
					print(); n+=1 # Новая линия
			switch(0); print() # Начальное значение = 0 #
			def create_key(key):
				global m, k
				with open("key.txt","w") as file_key: # Создаём ключ #
					m1=input(HEAD.Line["full-"]+"\nWrite the text: "); m=""
					for i in m1: # Если символ с малого регистра- заменить его на большой
						if i.islower(): 
							m+=i.upper()
						else: 
							m+=i
					if key=="random_key":
						import random
						k="" 
						length=len(m) # Берём длину сообщения для ключа #
						for i in range(length): # Рандомный ключ #
							rand=random.randint(0,25)
							k+=arr[rand] 
						print("Key: "+k)
					elif key=="your_key": # Записываем ключ в файл key.txt #
						k=input("Write the key: ")
						k*=len(m)//len(k)+1
						file_key.write(k) 
					else: 
						raise SystemExit
					file_key.write(k) # Записываем ключ в файл key.txt #
			def create_crypt(c):
				with open("crypt.txt","w") as file_crypt: # Создаём зашифрованное сообщение #
					for i,j in enumerate(m): # Перебираем символы в переменной 'm' (Зашифрованном тексте)#
						gg=(ord(j)+ord(k[i])) # Переводим символы в числа и складываем сумму #
						c+=chr(gg%26+ord('A')) # Делим полученное значение по модулю на 26, прибавляем число символа 'A' и переводим число в символ алфавита #
					print(HEAD.Line["full-"]+"\nEcrypted message: "+str(c)); file_crypt.write(c) # Записываем зашифрованное сообщение в файл key.txt #
			def create_decrypt(v,decrypt):
				if decrypt=="with_file":
					with open("crypt.txt","r") as file_crypt: 
						c=file_crypt.read() # Читаем зашифрованное сообщение #
					with open("key.txt","r") as file_key: 
						k=file_key.read() # Читаем ключ #
				elif decrypt=="without_file": # Расшифровываем сообщение с файла
					c=input("Write the Crypt-text: ")
					k=input("Write the Key: ")
					k*=len(c)//len(k)+1; 
				else: 
					raise SystemExit
				for i,j in enumerate(c): # Перебираем символы в переменной 'c' (Ключе) #
					gg=(ord(j)-ord(k[i])) # Переводим символы в числа и вычитаем сумму #
					v+=chr(gg%26+ord('A')) # Делим полученное значение по модулю на 26, прибавляем число символа 'A' и переводим число в символ алфавита #
				print("Decrypted message: "+str(v)+"\n"+HEAD.Line["full-"])
				if decrypt=="with_file": 
					print("Encrypted file: crypt.txt"); print("Key-file: key.txt\n"+HEAD.Line["full-"])
				elif decrypt=="without_file": 
					pass
				else: 
					raise SystemExit
			print(HEAD.Line["full-"]+"\n"+HEAD.Line["crpt"]+"\n"+HEAD.Line["full-"]) # Выбор между созданием и чтением зашифрованного сообщения #
			print("1) Create the Crypt and Key files")
			print("2) Create the Crypt and Key files (Disposable)")
			print("3) Read the Crypt-file with Key-file")
			print("4) Read the Crypt-text with Key\n"+HEAD.Line["full-"])
			try: # Вывод ошибки, если 'answer' != Integer числу #
				answer=int(input(">> Choose the Number: "))
				if answer==1: # Шифрование с вашим ключом
					create_key("your_key")
					create_crypt("")
					create_decrypt("","with_file") 
				elif answer==2: # Шифрование с рандомным ключом
					create_key("random_key"); 
					create_crypt("")
					create_decrypt("","with_file") 
				elif answer==3: # Чтение зашифрованного сообщения-файла при помощи ключа-файла #
					create_decrypt("","with_file") 
				elif answer==4: # Чтение зашифрованного сообщения при помощи ключа #
					create_decrypt("","without_file") 
				else: # Вывод сообщения, если мы указали вместо 1/2/3/4 иное целое число #
					print("Number is not Defined!") 
			except ValueError: # Вывод ошибки, если человек ввёл не целое число #
				print("[x] Error!")
				print("Write only Integer Numbers!\n") 
			except FileNotFoundError: # Вывод ошибки, если файлов в директории не было обнаружено #
				print("[x] Error!")
				print("Crypt/Key Files is not Defined!\n") 