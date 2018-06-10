head = lambda x: x[0]
tail = lambda x: x[1:len(x)]

scnd = lambda x: head(tail(x))
tail2 = lambda x: tail(tail(x))

def scanl1(func, List) -> list:
    if len(List) < 2: return [head(List)]
    else: return [head(List)] + scanl1(func,[func(head(List),scnd(List))]+tail2(List))
print(scanl1(lambda x,y: x+y, [1,2,3,4,5]))
