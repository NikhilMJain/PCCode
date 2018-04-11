a = [2,4,3,2,5,6,7,8,-2,-1,-4]
a.sort()
print(a)
i = 0
j = len(a) - 1
k = 4
while i<j:
    if a[i] + a[j] == k:
        print(a[i],a[j])
    if a[i] + a[j] < k:
        i += 1
    else:
        j -= 1

