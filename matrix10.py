a = [[1,0,1,0],[1,0,0,0],[1,0,0,0],[0,0,0,0]]

rowFlag = colFlag = 0

for i in range(4):
    if a[i][0] == 1:
        colFlag = 1
    if a[0][i] == 1:
        rowFlag = 1

for i in range(1,4):
    for j in range(1,4):
        if a[i][j] == 1:
            a[i][0] = a[0][j] = 1

for i in range(1,4):
    for j in range(1,4):
        if a[i][0] == 1 or a[0][j] == 1:
            a[i][j] = 1

for i in a:
    print i
