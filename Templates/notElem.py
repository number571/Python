head = lambda x: x[0]
tail = lambda x: x[1:len(x)]
def notElem(element, List) -> bool:
    if not List: return True
    elif element == head(List): return False
    else: return notElem(element, tail(List))
print(notElem(11,[4,5,2,3,1]))
