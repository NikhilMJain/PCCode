a = [1,1,2,3,4,5,3,4,2,66]
r = 0
for i in a:
    r ^= i

s = r & ~(r - 1)

s1 = 0
s2 = 0
for i in a:
    if i & s:
        s1 ^= i
    else:
        s2 ^= i

for i in a:
    s1 ^= i

for i in a:
    s2 ^= i

print(s1,s2)
