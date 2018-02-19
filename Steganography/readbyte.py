try:
	namefile = input("File name: ") 
	with open(namefile, "rb") as file:
		counter = 0 
		while byte:
			byte = file.read(1)
			print(byte)
			counter += 1
except FileNotFoundError: 
	print("[x] File: '{name}' is not defined!".format(name = namefile))
else:
	print("Number of bytes in the '{name}': {number}".format(name = namefile, number = counter))