head = lambda x: x[0]
tail = lambda x: x[1:len(x)]
def filter(func, List) -> list:
    if not List: return []
    elif func(head(List)): return [head(List)] + filter(func, tail(List))
    else: return filter(func, tail(List))
def qsort(List) -> list:
    if not List: return []
    else: return qsort(filter(lambda x: x < head(List), tail(List))) + [head(List)] + qsort(filter(lambda x: x >= head(List), tail(List)))
print(qsort([6,9,8,0,7,2,1,4,3,5]))
