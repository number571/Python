head = lambda x: x[0]
tail = lambda x: x[1:len(x)]
def mapp(func, listS, final = []):
	if not listS:
		return final
	else:
		final.append(func(head(listS)))
		return mapp(func, tail(listS))
print(mapp(lambda x: x * 2, [1,2,3,4,5]))
