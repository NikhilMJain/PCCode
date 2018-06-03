mat = [[10, 20, 30, 40], [15, 25, 35, 45], [26, 36, 46, 56], [71, 81, 91, 98]]

mini = 1
minj = 0
i = j = 0
maxi = maxj = len(mat) - 1
while maxi >= mini and minj < maxj:
    while j <= maxi:
        print  mat[i][j]
        j = j + 1
    j = j - 1
    i = i + 1
    maxj = maxj - 1

    while i <= maxi:
        print  mat[i][j]
        i = i + 1
    i = i - 1
    j = j - 1
    maxi = maxi - 1

    while j >= minj:
        print  mat[i][j]
        j = j - 1
    j = j + 1
    i = i - 1
    minj = minj + 1

    while i >= mini:
        print  mat[i][j]
        i = i - 1
    j = j + 1
    mini = mini + 1