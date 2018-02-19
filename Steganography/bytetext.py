with open(input("File-Cover: "), 'ab') as file: 
	file.write(input("Write the text: ").encode("utf-8")) 
	print("[+] File successfully overwritten!")