a = [11,13,21,3]
s = []

s.append(a[0])

for i in range(1, len(a)):
    while s and a[i] > s[-1]:
        print("{}-->{}".format(s.pop(), a[i]))
    s.append(a[i])
while s:
    print("{}-->{}".format(s.pop(), -1))