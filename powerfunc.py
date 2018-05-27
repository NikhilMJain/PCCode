def fun(x, n):
    res = 1
    for i in range(1, n + 1):
        res *= x
    print(res)

fun(2,3)