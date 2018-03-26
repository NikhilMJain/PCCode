a = [-7,1,5,2,-4,3,0]
sum = 0
for _ in a:
    sum += _
cur = 0
for i, _ in enumerate(a):
    
    sum -= _
    if cur == sum:
        print i
    cur += _