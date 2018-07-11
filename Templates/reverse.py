head = lambda x: x[0]
tail = lambda x: x[1:]
def reverse(List) -> list:
    if not List: return []
    else: return reverse(tail(List)) + [head(List)]
print(reverse([1,2,3,4,5]))

'''
last = lambda x: x[-1]
init = lambda x: x[:-1]
def reverse(List) -> list:
    if not List: return []
    else: return [last(List)] + reverse(init(List))
print(reverse([1,2,3,4,5]))
'''
