a = [12,1,78,90,57,89,56]
q = []
n = len(a)

k = 3

for i in range(k):
    while q and a[i] > a[q[-1]]:
        q.pop()
    q.append(i)

print(a[q[0]], end=' ')

for i in range(k, n):
    while i - k >= q[0]:
        q.pop(0)
    while q and a[i] > a[q[-1]]:
        q.pop()
    q.append(i)

    print(a[q[0]], end=',')

