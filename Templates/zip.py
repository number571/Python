head = lambda x: x[0]
tail = lambda x: x[1:len(x)]
def zip(List_one, List_two):
    if not List_one or not List_two: return []
    else: return [(head(List_one),head(List_two))] + zip(tail(List_one), tail(List_two))
print(zip([1,2,3],[4,5,6]))
