head = lambda x: x[0]
tail = lambda x: x[1:len(x)]
def dropWhile(func, List) -> list:
    if not func(head(List)): return List
    else: return dropWhile(func, tail(List))
print(dropWhile(lambda x: x < 5, [3,4,2,1,5,6,9,10]))
