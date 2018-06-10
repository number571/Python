head = lambda x: x[0]
tail = lambda x: x[1:len(x)]
def map(func, List) -> list:
    if not List: return []
    else: return [func(head(List))] + map(func, tail(List))
print(map(lambda x: x * 2, [1,2,3,4,5]))
