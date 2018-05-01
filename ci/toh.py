def toh(n, a, b, c):
    if n:
        toh(n - 1, a, c, b)
        print("{} to {}".format(a,c),end=",")
        toh(n-1, b,a,c)

toh(25,'a','b','c')