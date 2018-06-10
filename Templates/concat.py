head = lambda x: x[0]
tail = lambda x: x[1:len(x)]
def concat(ListOfLists) -> list:
    if not ListOfLists: return []
    else: return head(ListOfLists) + concat(tail(ListOfLists))
print(concat([[1,2,3],[4,5,6],[7,8,9]]))
