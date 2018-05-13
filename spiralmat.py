a = [
    [1,2,3,4,5,6],
    [7,8,9,10,11,12],
    [13,14,15,16,17,18]
]

i = j = mini = minj = 0
maxi = 3
maxj = 6

while mini < maxi and minj < maxj:
    i = mini
    j = minj

    while j < maxj:
        print(a[i][j],end=' ')
        j += 1
    maxj = j = j - 1
    i += 1

    while i < maxi:
        print(a[i][j],end=' ')
        i += 1
    maxi = i = i - 1
    j -= 1

    while j >= minj:
        print(a[i][j],end=' ')
        j -= 1
    minj = j = j + 1
    minj += 1
    i -= 1

    while i > mini:
        print(a[i][j],end=' ')
        i -= 1
    mini += 1
    j += 1