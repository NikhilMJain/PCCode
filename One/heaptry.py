import heapq

h = []

l = [2,3,1,4,8,7,65,9]
print(l)

for i in l:
    heapq.heappush(h, -i)

print(h)
# heapq.heapify(list(reversed(l)))
# print(l)
for i in l:
    print(-heapq.heappop(h),end=' ')

