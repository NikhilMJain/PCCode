import heapq
a = [4,3,1,7,6,5,4,8,9]
a = [-x for x in a]
heapq.heapify(a)

for i in range(4):
    print(-heapq.heappop(a))