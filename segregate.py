a = [0,3,2,4,5,6,7,8,9]
print a
l = 0
r = len(a) - 1

while l < r:
    while a[l] % 2 == 0:
        l += 1
    while a[r] % 2 != 0:
        r -= 1
    if l < r:
        a[l], a[r] = a[r], a[l]

print a

