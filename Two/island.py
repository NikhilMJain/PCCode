a = [
    [1, 1, 0, 0, 0],
    [0, 1, 0, 0, 1],
    [1, 0, 0, 1, 1],
    [0, 0, 0, 0, 0],
    [1, 0, 1, 0, 1] 
]

r = [-1, -1, -1, 0, 0, 1, 1, 1]
c = [-1, 0, 1, -1, 1, -1, 0, 1]

l = len(a)
vis = [[False for i in range(l)] for j in range(l)]

def search(i,j):
    if i >= l or j >= l or i < 0 or j < 0 or vis[i][j] == True or a[i][j] == 0:
        return
    
    vis[i][j] = True

    for k in range(len(r)):
        search(i + r[k], j + c[k])
    
def count_islands():
    count = 0

    for i in range(l):
        for j in range(l):
            if a[i][j] == 1 and vis[i][j] == False:
                search(i, j)
                count += 1
    return count

print(count_islands())