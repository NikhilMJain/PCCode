l = [1,2,3,4,5,6,7]
i = 0
k = 3
print l
t = a[(i + k) % len(l)]
while i< len(l):
    a[(i + k) % len(l) + 1] = t
    a[(i + k) % len(l)] = a[i]
    i = i + 1
    t = a[(i + k) % len(l)]
     

print l 
