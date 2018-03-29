c = 0
n = 1004
s = 0
print n
while n:
    rem = n % 10
    s = s + ((5 if rem == 0 else rem) * (10 ** c))
    n = n // 10
    c += 1
print s