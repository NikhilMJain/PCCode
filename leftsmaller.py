l = [1,3,4,5,2,1,3,4,5]
res = []
s = []
print l
for i in l:
    while s and s[-1] >= i:
        s.pop()
    if s:
        res.append(s[-1])
    else:
        res.append(-1)
    s.append(i)


print res