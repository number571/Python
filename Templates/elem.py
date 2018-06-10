head = lambda x: x[0]
tail = lambda x: x[1:len(x)]
def elem(element, List) -> bool:
    if not List: return False
    elif element == head(List): return True
    else: return elem(element, tail(List))
print(elem(3,[4,5,2,3,1]))
