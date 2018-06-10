tail = lambda x: x[1:len(x)]
def drop(num, List) -> list:
    if not num: return List
    else: return drop(num-1,tail(List))
print(drop(5,[1,2,3,4,5,6,7,8,9,10]))
