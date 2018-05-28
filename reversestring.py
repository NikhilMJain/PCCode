a = ['a','l','h','a','m','d','u','l','l','i','a','h']
print (a)
l = 0
r = len(a) - 1

while l<r:
    if l<r:
        a[l],a[r] = a[r],a[l]
    l = l+1
    r = r-1

print (a)