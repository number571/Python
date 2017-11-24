from Modules import HEAD, TERM
def choose(): 
	scan="" # Создаём нулевую переменную
	while scan not in TERM.Command_ADDT["Back"]: 
		scan=input("[root@"+TERM.Hostname+" scan]# ")
		if   scan in TERM.Command_SCAN["Scanner"]: scanner() # При двойке сработает функция scanner
		elif scan in TERM.Command_ADDT["Check"]: title() # Проверка модулей
		elif scan in TERM.Command_ADDT["Help"]: HEAD.help() # Предоставление информации о командах
		elif scan in TERM.Command_ADDT["Info"]: HEAD.info() # Дополнительная информация
		elif scan in TERM.Command_ADDT["Clear"]: HEAD.clear() # Очистка истории
		elif scan in TERM.Command_ADDT["Back"]: continue # Выход из модуля
		elif scan in TERM.Command_ADDT["Exit"]: raise SystemExit # Выход из программы
		else: print("?:",scan,":command not found") # Если не указаны вышеперечисленные условия

def title(): # Предоставление информации о модуле Scanners
	print(HEAD.Line["full-"]+"\n[>] Write the number:")
	print("\t1) SCANNER.571\n"+HEAD.Line["full-"])

def scanner(): # Ports/IP 
	import socket, os
	ports = [20, 21, 22, 23, 25, 42, 43, 53, 67, 69, 80, 110, 115, \
	123, 137, 138, 139, 143, 161, 179, 443, 445, 514, 515, 993, \
	995, 1080, 1194, 1433, 1702, 1723, 1900, 3128, 3268, 3306, \
	3389, 5432, 5060, 5900, 5938, 8080, 10000, 14900 ,20000] # Большинство возможных портов
	print(HEAD.Line["full-"]+"\n"+HEAD.Line["scan"]+"\n"+HEAD.Line["full-"])
	print("1) Scan Ports/Sites\n2) Scan Ports/IP\n3) Print your local IP\n4) Scan IP\n") 
	try: # Предотвращение ошибок
		answer=int(input("Write the Number: ")) 
		if answer==1:
			print ("\n"+HEAD.Line["full="]+"\n"+"\t\tPort scanner"+"\n"+HEAD.Line["full-"])
			host=input('IP/Site adress: ')
			print (HEAD.Line["full-"]+"\n"+"\t\tScanning!"+"\n"+HEAD.Line["full-"])
			for i in ports: # Время подключения 0.08c
				s=socket.socket()
				s.settimeout(0.08) 
				try: # Сканирование IP/Сайта на наличие открытых портов
					s.connect((host, i)) 
				except socket.error: # Если порт закрыт То ошибка пропускается и цикл переходит на следующий порт
					continue 
				else: # Вывод открытых портов
					s.close
					print (host+': '+str(i)+' Port is active') 
			print (HEAD.Line["full-"]+"\n"+"\t\tThe process is complete"+"\n"+HEAD.Line["full="]) # Конец программы
		elif answer==2: # Сканирование диапозона ip на наличие открытых портов
			print ("\n"+HEAD.Line["full="]+"\n"+"\t\tIP/Port scanner"+"\n"+HEAD.Line["full-"])
			print("192.168.[1?].[2?-3?]") 
			ans=input("Write the Number[1]: ")
			num1=int(input("Start_range  IP[2]: ")) # Начальное значение диапозона
			num2=int(input("End_range    IP[3]: ")) # Конечное значение диапозона
			host=("192.168.%s."%ans)
			print (HEAD.Line["full-"]+"\n"+"\t\tScanning!"+"\n"+HEAD.Line["full-"])
			for j in range(num1,(num2+1)): 
				for i in ports:
					s=socket.socket()
					s.settimeout(0.0013) # Время подключения 0.0013c
					ip=host+str(j) 
					try: # Сканирование IP диапозона на наличие открытых портов
						s.connect((ip, i)) 
					except socket.error: # Если закрыт порт, то ошибка пропускается и цикл переходит на следующий порт
						continue 
					else: # Вывод открытых ip и открытых портов
						print (ip+': '+str(i)+' Port is active') 
			s.close
			print (HEAD.Line["full-"]+"\n"+"\t\tThe process is complete"+"\n"+HEAD.Line["full="]) # Конец программы
		elif answer==3:
			print (HEAD.Line["full-"]+"\n"+"\t\tScanning!"+"\n"+HEAD.Line["full-"])
			print(socket.gethostbyname(socket.gethostname())) # Вывод вашего локального ip адреса
			print (HEAD.Line["full-"]+"\n"+"\t\tThe process is complete"+"\n"+HEAD.Line["full="]) # Конец программы
		elif answer==4: # Сканирование IP адресов при помощи ping
			print ("\n"+HEAD.Line["full="]+"\n"+"\t\tIP scanner"+"\n"+HEAD.Line["full-"])
			print("192.168.[1?].[2?-3?]")
			ans=input("Write the Number[1]: ")
			num1=int(input("Start_range  IP[2]: ")) # Начальное значение диапозона
			num2=int(input("End_range    IP[3]: ")) # Конечное значение диапозона
			host=("192.168.%s."%ans)
			print (HEAD.Line["full-"]+"\n"+"\t\tScanning!"+"\n"+HEAD.Line["full-"])
			for j in range(num1,(num2+1)):
				ip=host+str(j) # IP
				os.system("ping -c 1 -W 1 "+ip+" | grep 'from' && echo IP: "+ip+" is alive") # Команда в Linux'e
			print (HEAD.Line["full-"]+"\n"+"\t\tThe process is complete"+"\n"+HEAD.Line["full="]) # Завершение процесса
		else: # Вывод сообщения, если указанных чисел не существует в условии
			print("\n"+HEAD.Line["full="]+"\n"+"[x] Number is not Defined!"+"\n"+HEAD.Line["full="]) 
	except: # Вывод ошибки, если что-то пойдёт не так
		print("\n"+HEAD.Line["full="]+"\n"+"[x] Error!"+"\n"+HEAD.Line["full="]) 