a = [1,0,0,0,2,2,1,2,1,2,1,1,1,1,0,0,0,0]

l = 0
h = len(a) - 1
m = 0
while m <= h:
    if a[m] == 0:
        a[m], a[l] = a[l], a[m]
        m = m + 1
        l = l + 1
    elif a[m] == 1:
        m = m + 1
    elif a[m] == 2:
        a[m], a[h] = a[h], a[m]
        h = h - 1
print a