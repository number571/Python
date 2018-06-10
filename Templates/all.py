head = lambda x: x[0]
tail = lambda x: x[1:len(x)]
def all(func, List) -> bool:
    if not List: return True
    elif not func(head(List)): return False
    else: return all(func,tail(List))
print(all(lambda x: x > 3, [8,7,9,5,6]))
