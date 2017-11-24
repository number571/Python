from Modules import HEAD, TERM
def choose(): 
	stgn="" # Создаём нулевую переменную
	while stgn not in TERM.Command_ADDT["Back"]: 
		stgn = input("[root@"+TERM.Hostname+" stgn]# ")
		if   stgn in TERM.Command_STGN["Zip"]: zip() # При единице сработает функция zip
		elif stgn in TERM.Command_STGN["Message"]: message() # При единице сработает функция zip
		elif stgn in TERM.Command_STGN["Read-bytes"]: read_bytes() # При единице сработает функция read_bytes						
		elif stgn in TERM.Command_ADDT["Check"]: title() # Проверка модулей
		elif stgn in TERM.Command_ADDT["Help"]: HEAD.help() # Предоставление информации о командах
		elif stgn in TERM.Command_ADDT["Info"]: HEAD.info() # Дополнительная информация
		elif stgn in TERM.Command_ADDT["Clear"]: HEAD.clear() # Очистка истории
		elif stgn in TERM.Command_ADDT["Back"]: continue # Выход из модуля
		elif stgn in TERM.Command_ADDT["Exit"]: raise SystemExit # Выход из программы
		else: print("?:",stgn,":command not found") # Если не указаны вышеперечисленные условия

def title(): # Предоставление информации о модуле Steganography
	print(HEAD.Line["full-"]+"\n[>] Write the number:")
	print("\t1) ZIP.571\n\t2) MESSAGE.571\n"+HEAD.Line["nfull-"]+"\n\t0) READ_BYTES.571\n"+HEAD.Line["full-"])

def zip(): # Функция zip
	print(HEAD.Line["full-"]+"\n"+HEAD.Line["stgn"]+"\n"+HEAD.Line["full-"])
	try: 
		namefile=input("File-Cover: ") 
		with open(namefile, 'rb') as file1: # Чтение файла-оболочки
			read1=file1.read() 
	except FileNotFoundError: # Ошибка, если файл не был найден
		print("[x] File: '"+str(namefile)+"' is not defined!")
		raise SystemExit 
	try: 
		zipfile=input("Zip-File: ")
		with open(zipfile, 'rb') as file2: # Чтение zip-файла
			read2=file2.read() 
	except FileNotFoundError: # Ошибка, если zip-файл не был найден
		print("[x] File: '"+str(zipfile)+"' is not defined!")
		raise SystemExit 
	with open(namefile, 'wb') as file3: # Запись в файл оболочку zip-файл
		file3.write(read1) 
		file3.write(read2) 
	print(HEAD.Line["full-"]+"\n[+] File: "+str(namefile)+" successfully overwritten!\n"+HEAD.Line["full-"]) # Успешное завершение работы

def message(): # Функция message
	print(HEAD.Line["full-"]+"\n"+HEAD.Line["stgn"]+"\n"+HEAD.Line["full-"])
	try: 
		namefile=input("File-Cover: ") # Чтение имени файла
		with open(namefile, 'ab') as file: # Добавление в файл, на уровне байтов, сообщение
			text=input("Write the text: ")
			file.write(text.encode("utf-8")) 
	except FileNotFoundError: # Ошибка, если файл не был найден
		print("[x] File: '"+str(namefile)+"' is not defined!")
		raise SystemExit 
	print(HEAD.Line["full-"]+"\n[+] File: "+str(namefile)+" successfully overwritten!\n"+HEAD.Line["full-"]) # Успешное завершение работы

def read_bytes(): # Функция read_bytes
	print(HEAD.Line["full-"]+"\n"+HEAD.Line["stgn"]+"\n"+HEAD.Line["full-"])
	try:
		namefile=input("File name: ") # Чтение имени файла
		with open(namefile, "rb") as r: # Чтение файла побайтого
			byte = r.read(1) 
			k=0 # k- счётчик количества байт
			while byte: 
				byte = r.read(1) 
				print(byte)
				k+=1 
	except FileNotFoundError: # Ошибка, если файл не был найден
		print("[x] File: '"+str(namefile)+"' is not defined!")
		raise SystemExit 
	print("Number of bytes in the '"+str(namefile)+"': "+str(k)+"\n"+HEAD.Line["full-"]) # Успешное завершение работы