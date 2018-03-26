def QuickSort(a, l, h):
    if l < h:
        s = Partition(a, l, h)
        QuickSort(a, 0, s-1)
        QuickSort(a, s+1, h)

def Partition(a,l,h):
    p = a[h]
    c = i = 0
    while l <= h:
        if a[l] < p:
            a[i], a[l] = a[l], a[i]
            i = i+1
        l = l + 1
    a[i], a[h] = a[h], a[i]
    return i

l = [13,4,9,6,1]
print l
QuickSort(l,0,len(l)-1)
print l