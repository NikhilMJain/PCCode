grid = [
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0]
]
N = len(grid)
r = c = 0


def Is_Safe(i, c):
    return Row_Clash(i) and Col_Clash(c) and Diag_Clash(i, c)

def Row_Clash(r):
    for i in range(N):
        if grid[r][i] == 1:
            return False
    return True

def Col_Clash(c):
    for i in range(N):
        if grid[i][c] == 1:
            return False
    return True

def Diag_Clash(r, c):
    for i in range(c, -1, -1):
        if grid[r - i][c - i] == 1:
            return False
    for i in range(c, -1, -1):
        if i < N:
            if grid[r + i][c - i] == 1:
                return False
    return True






def Q(c):
    if c == N:
        return True
    
    for i in range(N):
        if Is_Safe(i, c):
            grid[i][c] = 1
            for j in grid:
                print(j)

            if Q(c + 1):
                return True
            
            grid[i][c] = 0
    return False

Q(0)

for i in grid:
    print(i)