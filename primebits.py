pb = [2,3,5,7,11,13,17]

l = 6
r = 10
c = 0
for i in range(l, r + 1):
    if str(bin(i))[2:].count('1') in pb:
        c += 1
print c