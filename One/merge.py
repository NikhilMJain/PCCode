import math
def MergeSort(a, n):
    if n > 1:
        b = a[0:(n//2)]
        c = a[(n//2):]
        MergeSort(b,len(b))
        MergeSort(c,len(c))
        Merge(b,c,a)

def Merge(b,c,a):
    i = j = k = 0
    while(i<len(b) and j<len(c)):
        if b[i] < c[j]:
            a[k] = b[i]
            i += 1
        else:
            a[k] = c[j]
            j += 1
        k += 1
    if i == len(b):
        while j < len(c):
            a[k] = c[j]
            k += 1
            j += 1
    else:
        while i < len(b):
            a[k] = b[i]
            k += 1
            i += 1

l = [13,4,9,6,1]
print l
MergeSort(l, len(l))
print l 