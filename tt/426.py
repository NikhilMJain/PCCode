# ##also, converttodll.py
# class Node():
#     def __init__(self, item = None):
#         self.info = item
#         self.next = None

class Node():
    def __init__(self, info = None):
        self.info = info
        self.l = self.r = None

# def sumlist(f, s):
#     head = None
#     c = 0
#     while f is not None or s is not None:
#         res = (f.info if f else 0) + (s.info if s else 0) + c
#         if res > 9:
#             c = 1
#             res %= 10
#         else:
#             c = 0
#         node = Node(res)
#         if head is None:
#             prev = head = node
#         else:
#             prev.next = node
#             prev = node
#         f = f.next if f else None
#         s = s.next if s else None
#     if c == 1:
#         prev.next = Node(1)
#     return head


# f = Node(8)
# f.next = Node(6)
# # f.next.next = Node(3)

# s = Node(4)
# s.next = Node(5)


# x = sumlist(f, s)
# print 
# c = 0

# def sumfrontsame(f,s):
    # global c

    # def inner(f, s):
    #     global c
    
    #     if f is None or s is None:
    #         return
        
    #     r = Node()

    #     r.next = inner(f.next, s.next)
    #     res = f.info + s.info + c
    #     if res > 9:
    #         c = 1
    #         res %= 10
    #     else:
    #         c = 0
    #     r.info = res
    #     return r

    # head = inner(f,s)
    # if c == 1:
    #     node = Node(1)
    #     node.next = head
    #     return node
    # return head

# def sumfrontdiff(f,s):
#     global c
    
#     def addFront(root, val):
#         node = Node(val)
#         node.next = root
#         return node

#     def length(head):
#         c = 0
#         while head:
#             c += 1
#             head = head.next
#         return c

#     def inner(f, s):
#         global c
    
#         if f is None or s is None:
#             return
        
#         r = Node()

#         r.next = inner(f.next, s.next)
#         res = f.info + s.info + c
#         if res > 9:
#             c = 1
#             res %= 10
#         else:
#             c = 0
#         r.info = res
#         return r

#     def getstart(head, diff):
#         for i in range(diff):
#             head = head.next
#         return head
    
#     lenf = length(f)
#     lens = length(s)
    
#     if lens == lenf:
#         head = inner(f,s)
#         if c == 1:
#             node = Node(1)
#             node.next = head
#             return node
#         return head
#     else:
#         if lensf > lens:
#             diff = lenf - lens
#             newf = getstart(lenf, diff)
#             head = inner(newf,s)
#             if c == 0:
#                 while diff:
                    
#                 addRem(hea)
#         else:
#             diff = lens - lenf
#             getstart(lens, diff)
    

# f = Node(8)
# f.next = Node(7)
# # f.next.next = Node(3)

# s = Node(3)
# s.next = Node(9)

# x = sumfront(f, s)
# print 
d = {}

root = Node(6)
root.l = Node(2)
root.l.l = Node(-8)
root.r = Node(14)
root.r.l = Node(13)
root.r.r = Node(15)
root.r.l.l = Node(7)

def topview(root, hd):
    def inner(root, hd):
        if root:
            if hd in d:
                d[hd].append(root.info)
            else:
                d[hd] = [root.info]
            inner(root.l, hd - 1)
            inner(root.r, hd + 1)
    inner(root,hd)

    for i in sorted(d):
        print d[i][0]

topview(root, 0)


