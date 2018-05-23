#!/usr/bin/python3

# Запускайте программу под root пользователем:
# $ chmod +x main.py
# $ sudo ./main.py

from os import system, listdir, mkdir, chdir, getcwd
from time import sleep

'''
# Раскомментировать, если пакет 'tor' не установлен
dist = ["apt-get install", "pacman -S"]
prog = ["tor"]
for i in dist:
	for j in prog:
		system("{dist} {prog}".format(dist = i, prog = j))
'''

# Директории со страницами сайта
www = [False,"/var/www/"]
onion = [False,"/var/www/onion/"]

# Директория с основными файлами сайта
main_files = "/var/lib/tor/onion/"

# Файлы связанные с сайтом
html_file = [False,"/var/www/onion/index.html"]
host_file = "/var/lib/tor/onion/hostname"
key_file = "/var/lib/tor/onion/private_key"

# Файл со всей информацией
readme = [False,"README.txt"]

# Конфигурационный файл тора
torrc = [False,"/etc/tor/torrc"]

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

# Проверка на наличие html файла
for name in listdir(onion[1]):
	if name == "index.html":
		html_file[0] = True
		break

# Создание html файла
if html_file[0] == False:
	with open(html_file[1],"w") as html:
		html.write('''
<!DOCTYPE html>
<html>
	<head>
		<title>Script_by_#571</title>
		<meta charset="utf-8">
	</head>
	<body>
		<p>Hello World!</p>
	</body>
</html> ''')
		print("File '{file}' created".format(file = html_file[1]))

# Чтение конфигурационного файла 'torrc'
# на наличие строк настройки
with open(torrc[1],"r") as tor:
	for string in tor:
		if string == string1 or string == string2:
			torrc[0] = True
			break

# Если строк не было обнаружено: добавить
# строки в файл 'torrc'
if torrc[0] == False:
	with open(torrc[1],"a") as tor:		
		tor.write(string1+"\n"+string2)
		print("Strings appended in the '{file}' file:".format(file = torrc[1]))
		print("'{0}'\n'{1}'".format(string1,string2))

# Запуск tor сервиса
system("systemctl start tor.service")
system("systemctl restart tor.service")

# Сон в одну секунду для обработки сервисов
sleep(1)

# Чтение хостнэйма сайта
with open(host_file,"r") as host:
	hostname = host.read()
	print("File '{file}' read".format(file = host_file))

# Чтение приватного ключа сайта
with open(key_file,"r") as key:
	private_key = key.read()
	print("File '{file}' read".format(file = key_file))

# Проверка на наличие README файла
for name in listdir(getcwd()):
	if name == readme[1]:
		readme[0] = True
		break

# Если было обновление или не было найдено файла README, то обновить или создать README
if www[0] == False or onion[0] == False or html_file[0] == False or readme[0] == False:
	with open(readme[1],"w") as info:
		info.write('''
Tor configuration: '''+torrc[1]+''':
-	'''+string1+'''
-	'''+string2+'''\n
HTML file: '''+html_file[1]+'''\n
Main files: '''+main_files+'''
-   hostname ['''+host_file+''']: 
'''+hostname+''' 
-	private_key ['''+key_file+''']:
'''+private_key+'''
Use this command for run tor service:
[for one time, after rebooting use this command again]
-	systemctl start tor.service
[for always time]
-	systemctl enable tor.service\n
Use this command for activate port 80:
[use in the directory: '''+onion[1]+''']
-	python3 -m http.server 80
''')
		if readme[0] == True:
			print("File '{file}' updated".format(file = readme[1]))
		else:
			print("File '{file}' created".format(file = readme[1]))

# Переход в директорию html файла
chdir(onion[1])

# Активация python сервера
system("python3 -m http.server 80")
