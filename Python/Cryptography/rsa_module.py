from rsa import newkeys
pub, priv = newkeys(1024)
print(str(pub) + "\n\n" + str(priv))
fileEncrypt = "encryptRSA.py"
fileDecrypt = "decryptRSA.py"
with open(fileEncrypt,"w") as encryptScript: 
	encryptScript.write('''
from rsa import encrypt, PublicKey
message = input("Write the message: ").encode("utf8")
fileName = "encryptMessage.txt"
encryptMessage = encrypt(message,'''+str(pub)+''')
with open(fileName,"wb") as file:
	file.write(encryptMessage)
	print("Encrypt message:\\n{message}\\n[+] File: '{name}' successfully saved!".format(message = str(encryptMessage), name = fileName))
''')
	print("[+] File: '{name}' successfully saved!".format(name = fileEncrypt)) 
with open(fileDecrypt,"w") as decryptScript: 
	decryptScript.write('''
from rsa import decrypt, PrivateKey
fileName = input("Write the filename: ")
with open(fileName,"rb") as file:
	decryptMessage = decrypt(file.read(),'''+str(priv)+''')
	print("Decrypted message:",str(decryptMessage.decode("utf8")))
''') 
	print("[+] File: '{name}' successfully saved!".format(name = fileDecrypt))
