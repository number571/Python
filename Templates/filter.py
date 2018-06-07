head, tail = lambda x: x[0], lambda x: x[1:len(x)]
def filter(func, List, final = []):
    if not List: return List
    elif func(head(List)): return [head(List)] + filter(func, tail(List))
    else: return filter(func, tail(List))
print(filter(lambda x: x > 2, [1,2,3,4,5]))
