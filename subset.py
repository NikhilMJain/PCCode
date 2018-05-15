a = [15, 22, 14, 26, 32, 9, 16, 8]
m = [0,0,0,0,0,0,0,0]
k = 53
a.sort()
n = len(a)
count = 0
def fun(i, s):
    global count
    count += 1
    if s  + a[i] > k:
        return

    elif s + a[i] == k:
        m[i] = 1
        for i in range(len(m)):
            if m[i] == 1:
                print(a[i],end=' ')
        m[i] = 0
        print()

    else:
        m[i] = 1
        for j in range(i + 1, n):
            fun(j, s + a[i])
        m[i] = 0
    
fun(0, 0)
print(count)