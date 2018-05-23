message = list(input("Write the message: "))
key = input("Write the key: ")
for symbol in range(len(message)):
    try: message[symbol] = chr(ord(message[symbol]) ^ int(key))
    except ValueError: message[symbol] = chr(ord(message[symbol]) ^ ord(key))
print("Final message:","".join(message))