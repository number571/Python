head = lambda x: x[0]
tail = lambda x: x[1:len(x)]
def unzip(List) -> (list,list):
    if not List: return ([],[])
    else: return ([head(List)[0]] + unzip(tail(List))[0], [head(List)[1]] + unzip(tail(List))[1])
print(unzip([(1, 4), (2, 5), (3, 6)]))
