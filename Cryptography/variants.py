def variants(s, n):
    if n == 1:
        for head in s:
            yield head
    else:
        for head in s:
            for tail in variants(s, n-1):
                yield head + tail

for itm in (variants("abc", 3)):
    print(itm)
