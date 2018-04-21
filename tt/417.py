# class Node():
#     def __init__(self, info = None):
#         self.info = info
#         self.l = self.r = None
# s = []
# s1 = []

# head = one = Node(1)
# two = Node(2)
# three= Node(3)
# four = Node(4)
# five = Node(5)
# six = Node(6)
# seven = Node(7)
# ten = Node(10)
# nine = Node(9)

# ten.l = nine
# ten.r = one
# nine.l = seven
# nine.r = two
# seven.l = four
# seven.r = three

# def anc(root, key, s ):
#     if root:
#         if root.info == key:
#             s.append(root.info)
#             return True
#         if anc(root.l, key,s) or anc(root.r, key,s):
#             s.append(root.info)
#             return True
# p = 4
# q = 7
# anc(ten, p, s)
# anc(ten, q, s1)


# for i in s:
#     if i in s1:
#         x = i
#         break

# print(abs(s1.index(x) - s.index(x)) if x == p or x == q else abs(s1.index(x) - s.index(x)) + 2)
# print (s, s1)
# #

# #efficient one for lca

# def lca(root, p, q):
#     if root:
#         if root.info == p or root.info == q:
#             print('first'+str(root.info))
#             return root
#         lc = lca(root.l, p, q)
#         rc = lca(root.r, p, q)

#         if (lc and rc):
#             print('second'+str(root.info))
#             return root
#         elif lc:
#             return lc
#         else:
#             return rc

# lc = lca(ten, 9, 111).info

class Node():
    def __init__(self, val):
        self.info = val
        self.next = self.arbit = None

def printlist(head):
    while head:
        print(head.info,id(head),head.arbit.info)
        head = head.next
def clone(head):
    cur = head
    while cur:
        node = Node(cur.info)
        node.next = cur.next
        cur.next = node
        cur = node.next
    cur = head
    while cur and cur.next:
        cur.next.arbit = cur.arbit.next
        cur = cur.next.next
    cur = head
    clonehead = cur.next
    while cur.next:
        t = cur.next
        cur.next = cur.next.next
        cur = t
    printlist(head)
    print
    printlist(clonehead)
    cur = clonehead



head = Node(1)
two = Node(2)
three= Node(3)
four = Node(4)
five = Node(5)
six = Node(6)
seven = Node(7)
ten = Node(10)
nine = Node(9)

head.next = two
two.next = three
three.next = four


head.arbit = three
two.arbit = four
three.arbit = two
four.arbit = head

clone(head)




        