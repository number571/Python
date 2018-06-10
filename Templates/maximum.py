head = lambda x: x[0]
tail = lambda x: x[1:len(x)]
max_ = lambda x,y: x if x > y else y
def maximum(List):
    if len(List) == 1: return head(List)
    else: return max_(head(List), maximum(tail(List)))
print(maximum([5,7,2,4,1,8,4,3]))
