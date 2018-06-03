# class Heap:
#     def __init__(self):
#         self.h = [0]

#     def heapify(self, i = 1):
#         l = 2 * i
#         r = l + 1
#         large = i

#         if l <= len(self.h) and self.h[l] > self.h[i]:
#             large = l
#         if r <= len(self.h) and self.h[r] > self.h[large]:
#             large = r
#         if large != i:
#             self.h[i], self.h[large] = self.h[large], self.h[i]
#             self.heapify(large)

#     def convertToHeap(self, l):
#         for i in range()

import heapq

minh = []
maxh = []

a = [1,6,3,2,5,7,4]

for i in a:
    heapq.heappush(maxh, -i)
    heapq.heappush(minh, i)

print(minh)
print(maxh)

for i in a:
    
    print((heapq.heappop(minh), -heapq.heappop(maxh)))


    # if len(maxh) % 2 == 0:
    #     heapq.heappush(minh, -(heapq.heappop(maxh)))
    #     print(
    
