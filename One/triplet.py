a = [12,-5,4,1,6,9]
a.sort()
s = 0
for i in range(len(a) - 2):
    l = i + 1
    r = len(a) - 1

    while l < r:
        if a[i] + a[l] + a[r] == s:
            print (a[i], a[l], a[r])
        if a[i] + a[l] + a[r] < s:
            l = l + 1
        else:
            r = r - 1




