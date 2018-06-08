head = lambda x: x[0]
tail = lambda x: x[1:len(x)]
def sum(List) -> float:
    if not List: return 0
    else: return head(List) + sum(tail(List))
print(sum([6,8,4,3,5]))
