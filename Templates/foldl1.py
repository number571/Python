head = lambda x: x[0]
tail = lambda x: x[1:len(x)]
def foldl1(func, List):
    if len(List) == 1: return head(List)
    else: return func(head(List), foldl1(func, tail(List)))
print(foldl1(lambda x,y: x+y, [1,2,3,4,5]))
