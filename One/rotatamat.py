a = [[10, 20, 30, 40], [15, 25, 35, 45], [26, 36, 46, 56], [71, 81, 91, 98]]
l =len(a)

def transpose():
    for i in range(l):
        for j in range(i + 1,l):
            a[i][j], a[j][i] = a[j][i], a[i][j]

def reverse():
    for j in range(l):
        for i in range(l / 2):
            a[i][j], a[l - 1 - i][j] = a[l - 1 - i][j], a[i][j]
for i in a:
    print i

transpose()
reverse()
print 
for i in a:
    print i
