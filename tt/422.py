# a =[
#     [1,0,1,1,1],
#     [1,1,0,0,1],
#     [1,1,1,1,1],
#     [1,1,1,1,0],
#     [1,1,1,1,1]
# ]

# mi = mj = 0
# m = a.copy()
# maxnow = 0
# for j in range(1, 5):
#     for i in range(1, 5):
#         if a[i][j] == 1:
#             m[i][j] = min(a[i - 1][j], a[i][j - 1], a[i - 1][j - 1]) + 1
#             if m[i][j] >= maxnow:
#                 maxnow = m[i][j]
#                 mi = i
#                 mj = j

# print(mi, mj)
# print(m)
a = [[0, 0, 2, 1, 1], [0, 0, 0, 0, 1], [0, 1, 4, 1, 1], [0, 6, 0, 1, 1],
     [9, 1, 1, 1, 1]]


def bs(a, l, r):
    while l <= r:
        m = (l + r) // 2
        if (m == 0 and a[m] == 1) or (a[m] == 1 and a[m - 1] == 0):
            return m
        if a[m] == 0:
            l = m + 1
        else:
            r = m - 1


# for i in a:
#     print(bs(i, 0, 4))

print(list(map(max, a)))
