a = [1,2,3,4,5,6,7,8,9,10]
key = 12

a.sort()

i = 0
j = len(a) - 1

while i <= j:
    if a[i]+a[j] == key:
        print a[i], a[j]
        i = i + 1
    else:
        if a[i] + a[j] > key:
            j = j - 1
        else:
            i += 1
