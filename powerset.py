a = ['a','b','c','d']
m = [0] * len(a)

def fun(l, r):
    global m, a
    if l > r:
        return

    print('{', end='')
    for i in range(len(m)):
        if m[i] == 1:
            print(a[i], end='')
    print('}', end=' ')


    for i in range(l, r):
        m[i] = 1
        fun(i + 1, r)
        m[i] = 0
    
fun(0, len(a))

