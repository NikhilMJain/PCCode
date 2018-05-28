a = [9,1,4,0,2,8,6,3,5]
n = len(a)
l = 0
r = n - 1
lm = rm = 0
res = 0
while l < r:
    if a[l] < a[r]:
        if a[l] > lm:
            lm = a[l]
        else:
            res += lm - a[l]
        l += 1
    else:
        if a[r] > rm:
            rm = a[r]
        else:
            res += rm - a[r]
        r -= 1

print(res)