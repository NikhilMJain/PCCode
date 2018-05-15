a = [ [ 1, 0, 1, 1,1 ], [ 1, 1, 1, 0,1 ], [ 0, 0,0, 1, 1 ],[ 0, 0, 0, 1,0 ],[ 0, 0,0, 1, 1 ] ]

n = 5
m = [[0 for i in range(n)] for j in range(n)]

#m[0][0] = 1
count = 0
def fun(i, j):
    global count
    count += 1
    if i >= 0 and i < n and j >= 0 and j < n and m[i][j] != 1:
        if i == n - 1 and j == n - 1:
            m[i][j] = 1
            for _ in m:
                print(_)
            m[i][j] = 0
            print()
        else:
            if a[i][j] == 1:
                m[i][j] = 1
                fun(i, j + 1)
                fun(i + 1, j)
                fun(i - 1, j)
                fun(i, j - 1)
                m[i][j] = 0
fun(0, 0)

print(count)