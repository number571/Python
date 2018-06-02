head = lambda x: x[0]
tail = lambda x: x[1:len(x)]
def map(func, listS, final = []):
	if not listS:
		return final
	else:
		final.append(func(head(listS)))
		return map(func, tail(listS))
print(map(lambda x: x * 2, [1,2,3,4,5]))
