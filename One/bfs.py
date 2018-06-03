a = [
 [0,1,1,0,0,0],
 [1,0,0,1,1,0],
 [1,0,0,0,1,0],
 [0,1,0,0,1,1],
 [0,1,1,1,0,1],
 [0,0,0,1,1,0]
]

v = [0] * 6

q = []

q.append(0)
v[0] = 1

while q:
    x = q.pop(0)
    
    print(x,)

    for i in range(len(a)):
        if a[x][i] == 1 and v[i] != 1:
            q.append(i)
            v[i] = 1
    
