class Node():
    def __init__(self, info = None):
        self.info = info
        self.l = self.r = None

import sys


# # def find(root, level, key):
# #     if root:
# #         if root.info == key:
# #             return level
# #         return find(root.l, level + 1, key) + find(root.r, level + 1, key)
# #     return 0

# # root = ten = Node(10)
# # two = Node(-2)
# # three= Node(3)
# # four = Node(4)
# # five = Node(5)
# # six = Node(6)
# # ten.l = two
# # ten.r = six
# # two.l = Node(8)
# # two.r = Node(-4)
# # six.l = Node(7)
# # six.r = Node(5)

# # print find(root, 0, 6)


# class LNode:
#     def __init__(self, info = None):
#         self.info = info
#         self.next = None

# d = {}

# def pair(head, s):
#     cur = head
#     while cur:
#         d[cur.info] = True
#         cur = cur.next
    
#     cur = head
#     while cur:
#         if s - cur.info in d:
#             print (cur.info, s - cur.info)
#             break
#         cur = cur.next
#     else:
#         print 'Nope'

# head = LNode(2)
# head.next = LNode(4)
# head.next.next = LNode(6)
# head.next.next.next = LNode(9)
# head.next.next.next.next = LNode(15)    
# pair(head, 10)

a = 'aaaabbbb'

i = 0 
l = len(a)
while i < l - 1:
    c = 1
    while i < (l - 1) and a[i] == a[i + 1]:
        i += 1
        c += 1
    print (str(a[i]) + str(c))
    i += 1




