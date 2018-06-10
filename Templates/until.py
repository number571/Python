def until(condition, func, num):
    if condition(num): return num
    else: return until(condition, func, func(num))
print(until(lambda x: x > 100, lambda x: x * 2, 1))
