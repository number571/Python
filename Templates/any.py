head = lambda x: x[0]
tail = lambda x: x[1:len(x)]
def any(func, List) -> bool:
    if not List: return False
    elif func(head(List)): return True
    else: return any(func,tail(List))
print(any(lambda x: x == 7, [8,7,9,5,6]))
