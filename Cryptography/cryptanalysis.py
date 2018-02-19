print('''
\t\t A = 8.17% \t N = 6.75% 
\t\t B = 1.49% \t O = 7.51%  
\t\t C = 2.78% \t P = 1.93%
\t\t D = 4.25% \t Q = 0.10%
\t\t E = 12.7% \t R = 5.99%
\t\t F = 2.23% \t S = 6.33%
\t\t G = 2.02% \t T = 9.06% 
\t\t H = 6.09% \t U = 2.76%
\t\t I = 6.97% \t V = 0.98%
\t\t J = 0.15% \t W = 2.36% 
\t\t K = 0.77% \t X = 0.15%
\t\t L = 4.03% \t Y = 1.97%
\t\t M = 2.41% \t Z = 0.05%
''') 
name = input("File-name: ")
text = "" 
try: 
	with open(name,"r") as file:
		original = file.read() 
except FileNotFoundError: 
	print("File is not found!") 
else:
	for symbol in original:
		if symbol !=" ": 
			text += symbol 
dict = set(text)
def check(words, char):
	k = 0 
	for i in words:
		if i == char: k += 1 
	return k 
var = 0
print("[*] Result: ")
for symbol in dict:
	stat = 100 * check(text,symbol) / len(text)
	if var%2 == 0:
		print("\t\t{0} - {1}%\t".format(symbol,round(stat,2)),end="")
	else:
		print("{0} - {1}%".format(symbol,round(stat,2)))
	var += 1
print()