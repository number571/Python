head = lambda x: x[0]
tail = lambda x: x[1:len(x)]
def filter(func, listS, final = []):
    if not listS:
        return final
    else:
        if func(head(listS)):
            final.append(head(listS))
        return filter(func, tail(listS))
print(filter(lambda x: x > 2, [1,2,3,4,5]))
