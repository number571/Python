head = lambda x: x[0]
tail = lambda x: x[1:len(x)]
def scanl(func, num, List) -> list:
    if not List: return [num]
    else: return [num] + scanl(func, func(num, head(List)), tail(List))
print(scanl(lambda x, y: x // y, 64, [4,2,4]))
