def f(s):
    if len(s) == 1:
        return s
    res = 0
    for i in s:
        res += int(i)
    return f(str(res))

print(f(str(294)))