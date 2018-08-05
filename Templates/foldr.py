head = lambda x: x[0]
tail = lambda x: x[1:len(x)]
def foldr(func, elem, List):
    if not List: return elem
    else: return func(head(List), foldr(func, elem, tail(List)))
print(foldr(lambda x,y: x * y, 1, [1,2,3,4,5,6]))
