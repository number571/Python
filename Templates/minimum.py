head = lambda x: x[0]
tail = lambda x: x[1:len(x)]
min_ = lambda x,y: x if x < y else y
def minimum(List):
    if len(List) == 1: return head(List)
    else: return min_(head(List), minimum(tail(List)))
print(minimum([5,7,2,4,1,8,4,3]))
