a = [
    [0,0,1,0,0,0],
    [1,0,0,0,0,0],
    [0,0,0,1,1,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,1,0]
]

v = []
s = []
ind = [0] * len(a)

for i in range(len(a)):
    for j in range(len(a)):
        if a[i][j] == 1:
            ind[j] += 1
for i in range(len(a)):
    if ind[i] == 0:
        s.append(i)
        v.append(i)

while s:
    x = s.pop(0)
    
    print(x, end="-->")
    for i in range(len(a)):
        if a[x][i] == 1 and i not in v:
            ind[i] -= 1
            if ind[i] == 0:
                s.append(i)
                v.append(i)


print (v)