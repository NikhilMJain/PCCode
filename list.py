a = [1,2,3,4,12,6,4,3,1]

l = 0
r = len(a) - 1

while l <= r:
    m = (l + r) // 2
    if a[m] > a[m-1] and a[m+1] < a[m]:
        print a[m]
        break
    if a[m-1]<a[m] and a[m] < a[m+1]:
        l += 1
    else:
        r -= 1
    