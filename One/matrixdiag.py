a = [[10, 20, 30, 40], [15, 25, 35, 45], [26, 36, 46, 56], [71, 81, 91, 98]]
l =len(a)
for i in range(l):
    k = i
    j = 0
    while k >= 0:
        print a[k][j]
        k -= 1
        j += 1
for j in range(1, l):
    k = j
    i = l - 1
    while k < l:
        print a[i][k]
        k += 1
        i -= 1
