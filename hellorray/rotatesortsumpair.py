a = [7,8,9,1,2,3,4]
al = len(a)

def findpivot():
    l = 0
    r = al - 1
    while l <= r:
        m = (l + r) // 2
        if a[m] > a[m+1]:
            return m+1
        if a[l]>a[m]:
            r = m - 1
        else:
            l = m + 1





def bs(l, r):
    while l <= r:
        m = (l + r) // 2
        if key == a[m]:
            return m
        if key > a[m]:
            r = m - 1
        else:
            l = m + 1
p = findpivot()        

key = 22
if key < a[al - 1] and key > a[p]:
    print bs(p, al - 1)
else:
    print bs(0, p - 1)


