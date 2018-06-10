head = lambda x: x[0]
tail = lambda x: x[1:len(x)]
def filter(func, List):
    if not List: return []
    elif func(head(List)): return [head(List)] + filter(func, tail(List))
    else: return filter(func, tail(List))
print(filter(lambda x: x > 2, [1,2,3,4,5]))
