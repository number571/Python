from hashlib import sha256

def encrypt(string):
	signature = sha256(string.encode()).hexdigest()
	return signature

staticPassword = encrypt("secret")
dinamicPassword = encrypt(input("Write the password: "))

if staticPassword == dinamicPassword:
	print("Password is True!")
else:
	print("Password is False!")