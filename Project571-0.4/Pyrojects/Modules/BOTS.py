from Modules import HEAD, TERM
def choose():
	bots=""
	while bots not in TERM.Command_ADDT["Back"]:
		bots=input("[root@"+TERM.Hostname+" bots]# ")
		if   bots in TERM.Command_BOTS["Parser"]: parser() # При единице активирует функцию парсер
		elif bots in TERM.Command_BOTS["Clicker"]: clicker() # При двойке активирует функцию автокликера
		elif bots in TERM.Command_BOTS["TorScript"]: tor_script() # При тройке активирует функцию тор скрипта
		elif bots in TERM.Command_ADDT["Check"]: title() # Вывод действующих модулей
		elif bots in TERM.Command_ADDT["Help"]: HEAD.help() # Вывод информации о командах
		elif bots in TERM.Command_ADDT["Info"]: HEAD.info() # Дополнительная информация
		elif bots in TERM.Command_ADDT["Clear"]: HEAD.clear() # Очистка истории		
		elif bots in TERM.Command_ADDT["Back"]: continue # Выход из модуля	
		elif bots in TERM.Command_ADDT["Exit"]: raise SystemExit # Выход из программы		 
		else: print("?:",bots,":command not found") # Если не указаны вышеперечисленные условия

def title(): # Предоставление информации о модуле Bots
	print(HEAD.Line["full-"]+"\n[>] Write the number:")
	print("\t1) PARSER.571\n\t2) CLICKER.571\n\t3) TORSCRIPT.571\n"+HEAD.Line["full-"])

def tor_script():
	print(HEAD.Line["full-"]+"\n"+HEAD.Line["bots"]+"\n"+HEAD.Line["full-"])
	with open("tor_script","w") as file:
		file.write('''
#!/usr/bin/python3
# Запускайте программу под root пользователем:
# $ chmod +x main.py
# $ sudo ./main.py
from os import system, listdir, mkdir, chdir
from time import sleep
# Раскомментировать, если пакет 'tor' не установлен:
# dist = ["apt-get install", "pacman -S"]
# prog = ["tor"]
# for i in dist:
#	 for j in prog:
#		 system("{dist} {prog}".format(dist = i, prog = j))
# Директории со страницами сайта
www = [False,"/var/www/"]
onion = [False,"/var/www/onion/"]
# Директория с основными файлами сайта
main_files = "/var/lib/tor/onion/"
# Файлы связанные с сайтом
html_file = "/var/www/onion/index.html"
host_file = "/var/lib/tor/onion/hostname"
key_file = "/var/lib/tor/onion/private_key"
# Файл со всей информацией
readme = "README.txt"
# Конфигурационный файл тора
torrc = "/etc/tor/torrc"
# Строки для настройки конфигурации файла torrc
string1 = "HiddenServiceDir /var/lib/tor/onion"
string2 = "HiddenServicePort 80 127.0.0.1:80"
# Проверка существования директории 'www'
for name in listdir("/var/"):
	if name == "www":
		www[0] = True
		break
# Если директория не существует - создать 'www'
if www[0] == False:
	mkdir(www[1])
	print("Directory '{dir}' created".format(dir = www[1]))
# Если директория существует - проверить существование директории 'onion'
else:
	for name in listdir(www[1]):
		if name == "onion":
			onion[0] = True
			break
# Если директория 'onion' не существует - создать 'onion'
if onion[0] == False:
	mkdir(onion[1])
	print("Directory '{dir}' created".format(dir = onion[1]))
# Создание html файла
with open(html_file,"w") as html:
	html.write(\'''
	<!DOCTYPE html>
	<html>
		<head>
			<title>Script_by_#571</title>
			<meta charset="utf-8">
		</head>
		<body>
			<p>Hello World!</p>
		</body>
	</html> \''')
	print("File '{file}' created".format(file = html_file))
# Чтение конфигурационного файла 'torrc'
# на наличие строк настройки
operation = False
with open(torrc,"r") as tor:
	for i in tor:
		if i == string1 or i == string2:
			operation = True
			break
# Если строк не было обнаружено: добавить
# строки в файл 'torrc'
if operation == False:
	with open(torrc,"a") as tor:		
		tor.write(string1+"\\n"+string2)
		print("Strings appended in the '{file}' file:".format(file = torrc))
		print("'{0}'\\n'{1}'".format(string1,string2))
# Запуск tor сервиса
system("systemctl start tor.service")
system("systemctl restart tor.service")
# Сон в одну секунду для обработки сервисов
sleep(1)
# Чтение хостнэйма сайта
with open(host_file,"r") as host:
	hostname = host.read()
	print("File '{file}' created".format(file = host_file))
# Чтение приватного ключа сайта
with open(key_file,"r") as key:
	private_key = key.read()
	print("File '{file}' created".format(file = key_file))
# Создание вспомогающего файла
with open(readme,"w") as info:
	info.write(\'''
	Tor configuration: \'''+torrc+\''':
	-	\'''+string1+\'''
	-	\'''+string2+\'''\\n
	HTML file: \'''+html_file+\'''\\n
	Main files: \'''+main_files+\'''
	-   hostname [\'''+host_file+\''']: 
	\'''+hostname+\''' 
	-	private_key [\'''+key_file+\''']:
	\'''+private_key+\'''
	Use this command for run tor service:
	[for one time, after rebooting use this command again]
	-	systemctl start tor.service
	[for always time]
	-	systemctl enable tor.service\\n
	Use this command for activate port 80:
	[use in the directory: \'''+html_file+\''']
	-	python3 -m http.server 80
	\''')
	print("File '{file}' created".format(file = readme))
# Переход в директорию html файла
chdir(onion[1])
# Активация python сервера
system("python3 -m http.server 80") ''')
		print("[+] File 'tor_script' successfully saved!\n"+HEAD.Line["full-"])

def parser():
	try:
		from bs4 import BeautifulSoup
		import requests, time, fake_useragent
		print(HEAD.Line["full-"]+"\n"+HEAD.Line["bots"]+"\n"+HEAD.Line["full-"])
		ua=fake_useragent.UserAgent() 
		user=ua.random  # Создание рандомного юзер-агента
		headers={'User-Agent':str(user)} # Редактирование юзер-агента
		print(HEAD.Line["full-"]+"\n"+"[*] IP your network: ")
		main='http://icanhazip.com' # Сайт проверяющий глобальные ip адреса
		my_ip = requests.get(main,headers=headers) # Замена юзер-агента
		print("    "+str(my_ip.text)+HEAD.Line["full-"]) # Вывод информации о вашем глобальном ip адресе
		print("[*] Connecting to the Tor network /",end="") # Присоединение к сети tor
		proxies={ # Использование прокси tor'a
			'http': 'socks5h://127.0.0.1:9050', 
			'https': 'socks5h://127.0.0.1:9050'} 
		ip=requests.get(main,proxies=proxies,headers=headers) # Замена прокси сервера
		from time import sleep
		for i in range(10): 
			sleep(0.2)
			print('.', end='', flush=True)
		print("/\n[+] Connected to the Tor network")
		print(HEAD.Line["full-"]+"\n"+"[*] IP Tor network:")
		print("    "+str(ip.text)+HEAD.Line["full-"]) # Подключение к сети tor
		site="" # Создание нулевой переменной
		answer=input("[*] Parse something site?\n[y/n] > ") # Парсинг сайтов
		if answer=="y" or answer=="Y":
			print(HEAD.Line["full-"]+"\n"+"[*] Example: google.com") # Пример использования программы
			while site!="exit":
				print(HEAD.Line["full-"]+"\n"+"[!] Write the 'exit' if you are want exit from program") # 'exit' чтобы остановить программу
				site=input("    Write the hostname site: ") # Имя сайта, к примеру: ss4jioelrcp3nqq6.onion
				if site=="exit": break # Остановка цикла
				else: # Если указан сайт:
					data=requests.get("http://"+str(site),proxies=proxies,headers=headers) # Подключение к сайту с прокси и юзер-агентом
					print(HEAD.Line["full-"]+"\n"+"[*] Choose the number: ") 
					print("\t1) Save html code in the index.html") # Сохранение html кода
					print("\t2) Print html code in the terminal") # Вывод html кода в терминал
					print("\t3) Save links in the links.txt") # Сохранение ссылок
					print("\t4) Print links in the terminal") # Вывод ссылок в терминал
					print("\t5) Method 'Tree' (HTML)") # Метод 'tree', автоматически сохраняет html код в файл
					print("\t6) Method 'Tree' (LINKS)") # Метод 'tree', автоматически сохраняет ссылки в файл
					ans=int(input("[Number] > "))
					print(HEAD.Line["full-"]) 
					if ans==1:
						html=data.text # Копирование кода со страницы
						soup=BeautifulSoup(html, 'html.parser') # Парсинг html кода 
						with open("index.html","w") as file: # Копирование html кода с табуляцией в файл
							file.write(soup.prettify()) 
						print("[+] File: 'index.html' successfully saved ")
					elif ans==2:
						html=data.text # Копирование кода со страницы
						soup = BeautifulSoup(html, 'html.parser') # Парсинг html кода 
						print(soup.prettify()) # Копирование html кода и вывод в терминал
					elif ans==3:
						html=data.text # Копирование кода со страницы
						soup=BeautifulSoup(html, 'html.parser') # Парсинг html кода
						with open("links.txt","w") as file: # Создание файла
							for i in (soup.find_all("a")): # Сохранение всех <a href=""> в файл
								file.write(i.get("href")) 
							print("[+] File: 'links.txt' successfully saved ")
					elif ans==4:
						html=data.text # Копирование кода со страницы
						soup=BeautifulSoup(html, 'html.parser') # Парсинг html кода 
						for i in (soup.find_all("a")): # Вывод всех <a href=""> в терминал
							print(i.get("href")) 
					elif ans==5: # Метод 'TREE' (html)
						html=data.text # Копирование кода со страницы
						soup=BeautifulSoup(html, 'html.parser') # Парсинг html кода 
						with open("tree.html","w") as file: # Создание файла
							for i in (soup.find_all("a")): # Копирование всех <a></a>
								file.write("\n"+HEAD.Lines.h_line0()+"\n"+i.get("href")+": "+"\n") # Сохранение всех <a href=""> в файл
								try:
									datas=requests.get((i.get("href")),proxies=proxies,headers=headers) # Переход по ссылке
									htmls=datas.text # Копирование кода со страницы
									soups = BeautifulSoup(htmls, 'html.parser') # Парсинг html кода 
									file.write(HEAD.Line["full-"]+"\n"+soups.prettify()) # Сохранение html кода в файл
								except: # При нахождении ошибки пропуск на следующий ход цикла
									continue 
								print("[+] File: 'tree.html' successfully saved")
					elif ans==6: # Метод 'TREE' (ссылки)
						html=data.text # Копирование кода со страницы
						soup=BeautifulSoup(html, 'html.parser') # Парсинг html кода 
						with open("tree_links.txt","w") as file: # Создание файла
							for i in (soup.find_all("a")): # Копирование всех <a></a>
								file.write("\n"+HEAD.Line["full-"]+"\n"+i.get("href")+": "+"\n"+HEAD.Line["full-"]+"\n") # Сохранение всех <a href=""> в файл
								try:
									datas=requests.get((i.get("href")),proxies=proxies,headers=headers) # Переход по ссылке
									htmls=datas.text # Копирование кода со страницы
									soups = BeautifulSoup(htmls, 'html.parser') # Парсинг html кода 
									for j in (soups.find_all("a")): # Сохранение всех <a href=""> в файл	
										file.write(j.get("href")+"\n") 						
								except: # При нахождении ошибки пропуск на следующий ход цикла
									continue 
								print("[+] File: 'tree_links.txt' successfully saved")
					else: 
						print("[x] Only Integer numbers: 1,2,3,4,5,6!")
					print(HEAD.Line["full-"]+"\n"+"[x] Stopping connect to the Tor network"+"\n"+HEAD.Line["full-"]) # Завершение программы
		else: # Завершение программы
			print(HEAD.Line["full-"]+"\n"+"[x] Stopping connect to the Tor network"+"\n"+HEAD.Line["full-"]) 
	except: # Завершение программы
		print(HEAD.Line["full-"]+"\n"+"[x] Stopping connect to the Tor network"+"\n"+HEAD.Line["full-"]) 

def clicker(): # Автокликер
	print(HEAD.Line["full-"]+"\n"+HEAD.Line["bots"]+"\n"+HEAD.Line["full-"])
	with open("script.py","w") as file: 
		file.write("from pyautogui import *\nfrom time import sleep\n") # Действующие модули
	print('''---------------------------------------------------------------
[!] Recommend use the program 
    "Screen Loupe 2000"
    for coordinates - x,y''')
	text=('''---------------------------------------------------------------
0) sleep(x) <- Time of sleep in the seconds # Программа в режиме бездействия, x- количество секунд
---------------------------------------------------------------
1) moveTo(x,y) <- Move mouse # Перемещение курсора мыши на координаты x,y
2) click(x,y) <- Left click mouse # Клик мыши на координаты x,y
3) rightClick(x,y) <- Right click mouse # Правый клик мыши на координаты x,y
4) middleClick(x,y) <- Middle click mouse # Средний клик мыши на координаты x,y
5) doubleClick(x,y) <- Double Left click mouse # Двойной клик левой кнопки мыши на координаты x,y
---------------------------------------------------------------
6) typewrite(text) <- print your text # Печатать текст
7) press(key) <- produces the action of a key # Нажать клавишу
8) keyDown(key) <- press the key # Зажать клавишу
9) keyUp(key) <- let off the key # Отпустить клавишу
10) hotkey(key1,key2) <- key combination # Комбинация клавиш
---------------------------------------------------------------
99) Stop the program # Остановить программу
100) Print this text again # Вывести сообщение подсказки ещё раз
---------------------------------------------------------------''')
	print(text)
	with open("script.py","a") as file: # Редактирование кода
		ansc=100 # Начальное нулевое значение
		while ansc!=99: 
			try:
				ansc=int(input("Write the number: "))
				if ansc==0:
					x=int(input("Write the number 'x': "))
					file.write("sleep("+str(x)+")\n") # time.sleep(x)
				elif ansc in range(1,6):
					x=int(input("Write the number 'x': ")) # coordinate x
					y=int(input("Write the number 'y': ")) # coordinate y
					if ansc==1: # pyautogui.moveTo(x,y)
						file.write("moveTo("+str(x)+","+str(y)+")\n") 
					elif ansc==2: # pyautogui.click(x,y)
						file.write("click("+str(x)+","+str(y)+")\n") 
					elif ansc==3: # pyautogui.rightClick(x,y)
						file.write("rightClick("+str(x)+","+str(y)+")\n") 
					elif ansc==4: # pyautogui.middleClick(x,y)
						file.write("middleClick("+str(x)+","+str(y)+")\n") 
					elif ansc==5: # pyautogui.doubleClick(x,y)
						file.write("doubleClick("+str(x)+","+str(y)+")\n") 
				elif ansc==6:
					x=input("Write the text: ")
					file.write("typewrite('"+str(x)+"')\n") # pyautogui.typewrite(text)
				elif ansc in range(7,10):
					x=input("Write the key: ")
					if ansc==7: # pyautogui.press(key)
						file.write("press('"+str(x)+"')\n") 
					elif ansc==8: # pyautogui.keyDown(key)
						file.write("keyDown('"+str(x)+"')\n") 
					elif ansc==9: # pyautogui.keyUp(key)
						file.write("keyUp('"+str(x)+"')\n") 
				elif ansc==10: 
					x=input("Write the key1: ") # Комбинация клавиши 1
					y=input("Write the key2: ") # Комбинация клавиши 2
					file.write("hotkey('"+str(x)+"','"+str(y)+"')\n") # pyautogui.hotkey(key1,key2)
				elif ansc==100: # Вывод информации снова
					print(text) 
				elif ansc==99: # Закрытие программы
					pass 
				else: # При отсутствии числа в условиях
					print("Number is not defined!") 
			except: # Ошибка при обозначении не целого числа под переменными
				print("Error! Only Integer numbers!") 
			print(HEAD.Line["full-"]+"\n[+] File 'script.py' successfully saved!\n"+HEAD.Line["full-"])