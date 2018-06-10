head = lambda x: x[0]
tail = lambda x: x[1:len(x)]
def foldl(func, elem, List):
    if not List: return elem
    else: return foldl(func, func(elem, head(List)), tail(List))
print(foldl(lambda x,y: x/y, 64, [4,2,4]))
