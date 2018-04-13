import time
count = 0
# grid = [[3, 0, 6, 5, 0, 8, 4, 0, 0], 
#         [5, 2, 0, 0, 0, 0, 0, 0, 0],
#         [0, 8, 7, 0, 0, 0, 0, 3, 1], 
#         [0, 0, 3, 0, 1, 0, 0, 8, 0], 
#         [9, 0, 0, 8, 6, 3, 0, 0, 5],
#         [0, 5, 0, 0, 9, 0, 6, 0, 0], 
#         [1, 3, 0, 0, 0, 0, 2, 5, 0], 
#         [0, 0, 0, 0, 0, 0, 0, 7, 4], 
#         [0, 0, 5, 2, 0, 6, 3, 0, 0]]

grid = [[8, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 3, 6, 0, 0, 0, 0, 0],
        [0, 7, 0, 0, 9, 0, 2, 0, 0], 
        [0, 5, 0, 0, 0, 7, 0, 0, 0], 
        [0, 0, 0, 0, 4, 5, 7, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 3, 0], 
        [0, 0, 1, 0, 0, 0, 0, 6, 8], 
        [0, 0, 8, 5, 0, 0, 0, 1, 0], 
        [0, 9, 0, 0, 0, 0, 4, 0, 0]]
        
# grid = [[1,2,3,3,3,3,0,0,0],
# [0,0,0,0,0,0,1,2,3],
# [0,0,0,1,2,3,0,0,0],
# [2,3,1,0,0,0,0,0,0],
# [0,0,0,0,0,0,2,3,1],
# [0,0,0,2,3,1,0,0,0],
# [3,1,2,0,0,0,0,0,0],
# [0,0,0,0,0,0,3,1,2],
# [0,0,0,3,1,2,0,0,0]]

r = c = 0
gridlen = 9
def Find_Next():
    global r, c
    for i in range(gridlen):
        for j in range(gridlen):
            if grid[i][j] == 0:
                r = i
                c = j
                return True
    return False

def Is_Safe(row, col, num):
    return Col_Clash(col, num) and Row_Clash(row, num) and Box_Clash(row, col, num)

def Col_Clash(col, num):
    for i in range(gridlen):
        if grid[i][col] == num:
            return False
    return True

def Row_Clash(row, num):
    for i in range(gridlen):
        if grid[row][i] == num:
            return False
    return True

def Box_Clash(row, col, num):
    rstart = (row // 3) * 3
    cstart = (col // 3) * 3
    for i in range(rstart, rstart + 3):
        for j in range(cstart, cstart + 3):
            if grid[i][j] == num:
                return False
    return True


def Sudoku():
    global count
    if not Find_Next():
        return True
    rr = r
    cc = c
    for i in range(1, 10):
        if Is_Safe(rr, cc, i):
            grid[rr][cc] = i

            if Sudoku():
                return True

            grid[rr][cc] = 0

    return False

x = time.time()
print(Sudoku())
print(time.time() - x)
for i in grid:
    print(i)

