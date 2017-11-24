from Modules import HEAD, TERM # Импорт основных модулей
from Modules import STNR, MLWR, CRPT, BRFR, BOTS, SCAN # Импорт функциональных модулей
def Root(): # Главная функция
	Bool = True # Отображение титульной части (True = ON; False = OFF)
	HEAD.clear()
	HEAD.start(Bool)
	main = "" # Объявление главной переменной
	try: # Проверка на ошибки
		while main not in TERM.Command_ADDT["Exit"]: # Программа работает пока не вызовется команда завершения работы
			main = input("[root@"+TERM.Hostname+"~]# ") # Ввод и чтение переменной main 
			if   main in TERM.Command_MAIN["Cryptography"]: CRPT.choose() # Связывает с функциями Криптографии
			elif main in TERM.Command_MAIN["Scanners"]: SCAN.choose() # Связывает с функциями Сканеров
			elif main in TERM.Command_MAIN["Bots"]: BOTS.choose() # Связывает с функциями Ботов
			elif main in TERM.Command_MAIN["BruteForce"]: BRFR.choose() # Связывает с функциями Брутфорса
			elif main in TERM.Command_MAIN["Malware"]: MLWR.choose() # Связывает с функциями Вредоносного ПО
			elif main in TERM.Command_MAIN["Steganography"]: STNR.choose() # Связывает с функциями Стеганографии
			elif main in TERM.Command_MAIN["Components"]: HEAD.setup() # Установка компонентов
			elif main in TERM.Command_ADDT["Check"]: HEAD.title() # Просмотр модулей
			elif main in TERM.Command_ADDT["Help"]: HEAD.help() # Просмотр команд
			elif main in TERM.Command_ADDT["Info"]: HEAD.info() # Дополнительная информация
			elif main in TERM.Command_ADDT["Clear"]: HEAD.clear() # Очистка истории
			elif main in TERM.Command_ADDT["Exit"]: HEAD.stop(Bool) # Выход из программы
			else: print("?:",main,":command not found") # Вывод сообщения, если значение не было найдено 
	except: # Завершение программы
		print()
		HEAD.stop(Bool)
if __name__ == "__main__": # Запуск главной функции из файла файла
	Root()
else: # Иначе выход из программы
	print("[user@"+host+"~]$ python: cannot open '"+__name__+".py': Permission denied") 
	raise SystemExit