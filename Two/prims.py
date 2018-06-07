from math import inf

mat = [
    [inf,3,7,inf,inf,inf],
    [3,inf,inf,2,inf,1],
    [7,inf,inf,inf,6,inf],
    [inf,2,inf,inf,inf,5],
    [inf,inf,6,inf,inf,4],
    [inf,1,inf,5,4,inf]
]

mat = [[inf, 2, inf, 6, inf],
    [2, inf, 3, 8, 5],
    [inf, 3, inf, inf, 7],
    [6, 8, inf, inf, 9],
    [inf, 5, 7, 9, inf],]
l = len(mat)
v = []
k = [inf] * l
p = [-1] * l
vis = [False] * l
k[0] = 0


def getMin():
    m = inf
    for i in range(len(k)):
        if k[i] < m and not vis[i]:
            m = k[i]
            ver = i
    return ver


while len(v) < l:
    x = getMin()
    v.append(x)
    vis[x] = True
    for i in range(l):
        if mat[x][i] != inf and not vis[i]:
            if k[i] > mat[x][i]: 
                k[i] = mat[x][i]
                p[i] = x

for i in range(1, l):
    print(str(p[i]) + '-->' + str(i) + ': ' + str(mat[p[i]][i]))
