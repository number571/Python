head = lambda x: x[0]
tail = lambda x: x[1:len(x)]
def zipWith(func, List_one, List_two) -> list:
    if not List_one or not List_two: return []
    else: return [func(head(List_one),head(List_two))] + zipWith(func, tail(List_one), tail(List_two))
print(zipWith(lambda x,y: x + y, [1,2,3], [4,5,6]))
