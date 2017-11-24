Line = { # Линии для разделения текста
	"full-" :  "---------------------------------------------------------------",
	"full=" :  "===============================================================",
	"start" :  "------------------------Program_by_#571------------------------",
	"stop"  :  "------------------------Program_Stopped------------------------",
	"crpt"  :  "---------------------Cryptography_by_#571----------------------",
	"scan"  :  "-----------------------Scanners_by_#571------------------------",
	"bots"  :  "-------------------------Bots_by_#571--------------------------",
	"brtf"  :  "----------------------BruteForce_by_#571-----------------------",
	"mlwr"  :  "------------------------Malware_by_#571------------------------",
	"stgn"  :  "---------------------Steganography_by_#571---------------------",
	"nfull-":  "    -----------------------------------------------------------"}

def info(): # Дополнительная информация
	name="[*] Program by #571"
	version="[*] Version: 0.4"
	site="[*] Site: ss4jioelrcp3nqq6.onion"
	git="[*] Git: github.com/Number571"
	quantity="[*] Programs: 22"
	print((Line["full-"]+"\n%s\n%s\n%s\n%s\n%s\n"+Line["full-"])%(name,version,quantity,site,git))

def clear(): # Функция очистки истории
	from sys import platform; from os import system
	if platform == "linux": 
		system("clear")
	elif platform == "darwin": 
		system("clear")
	elif platform == "win32": 
		system("cls")

def help(): # Основная информация о командах
	print(Line["full-"]+"\n[*] \t\tInformation:")
	print("[1] You can use numbers instead name directories or files.")
	print("[2] Directories = '/'\n[3] Files = '.571'")
	print(Line["full-"]+"\n[*] \t\tTerminal Commands:")
	print("[1] '!' or 'info' or ':i' == Iformation about program.")
	print("[2] '?' or 'help' or ':h' == Full information commands.")
	print("[3] '/' or 'ls' or 'dir' or ':l' == Check directory.")
	print("[4] '<' or 'cd ..' or 'back' or ':b' == Back to Main directory.")
	print("[5] '&' or 'clear' or 'wash' or':c' == Clear the history.")
	print("[6] '$' or 'exit' or 'quit' or ':q' == Exit from program.")
	print("[7] '1' (just number) == Move to directory or run a program.")
	print("[8] 'cd *directory*' or ':d *directory*' == Move to directory.")
	print("[9] './*program*' or ':f *program*'== Run a program.\n"+Line["full-"])

def setup(): # Установка компонентов
	from sys import platform; from os import system
	arr1=["sudo apt-get install","sudo pacman -S","sudo emerge","sudo yum install"] # Debian/Arch/Gentoo/Fedora
	arr2=["socket","bs4","requests","fake_useragent","rsa","pyautogui","pyAesCrypt","threading","tkinter"] # Модули Python'a
	arr3=[" python-setuptools"," nmap"," tor"," tk"," python-xlib"] # Программы необходимые для функционирования
	if platform == "linux":
		print("Installing Components...")
		for j in arr3: # Установка программ для Linux
			for i in arr1: 
				system(str(i)+str(j)) 
		print("Installing pip3..."); system("sudo easy_install pip") # Установка pip3
		print("Installing modules for Python3...")
		for i in arr2: 
			system("sudo pip3 install "+str(i)) # Установка модулей из arr2
	elif platform == "win32":
		print("Installing modules for Python3...")
		for i in arr2: 
			system("pip3 install "+str(i)) # Установка модулей из arr2

def title(): # Информация о модулях
	print(Line["full-"]+"\n|[>] Choose the number:        |//////////////////////////////|")
	print("|-------------------------------------------------------------|")
	print("| 1) /Cryptography             |------------------------------|")
	print("| 2) /Scanners                 |   #   #     #####  #####   # |")
	print("| 3) /Bots                     | # # # # #   #          #   # |")
	print("| 4) /BruteForce               |   #   #     #####     #    # |")
	print("| 5) /Malware                  | # # # # #       #    #     # |")
	print("| 6) /Steganography            |   #   #     #####   #      # |")
	print("||||||||||||||||||||||||||||||||------------------------------|")
	print("|-------------------------------------------------------------|")
	print("| 0) COMPONENTS.571            |//////////////////////////////|\n"+Line["full-"])

def look(): # Информация для новичков
	print("[!] If you are running the program for the first time then\nrecommended install components: './COMPONENTS.571' or './0'\n"+Line["full-"])
	print("[*] Write the '?' if you are want saw a full information!\n[*] Write the '!' if you are want saw info about program!")
def start(boolean): # Показ старта программы
	if boolean: 
		print(Line["start"]+"\n"+Line["full-"])
		look(); title();
def stop(boolean): # Показ завершения программы
	if boolean: 
		print(Line["full-"]+"\n"+Line["stop"])