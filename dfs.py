a = [
 [0,1,1,0,0,0],
 [1,0,0,1,1,0],
 [1,0,0,0,1,0],
 [0,1,0,0,1,1],
 [0,1,1,1,0,1],
 [0,0,0,1,1,0]
]

v = [0] * 6


s = []

s.append(0)
v[0] = 1

while s:
    x = s.pop()
    
    print(x,end=' ')

    for i in range(len(a)):
        if a[x][i] == 1 and v[i] != 1:
            s.append(i)
            v[i] = 1
    
