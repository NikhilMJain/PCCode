# a =[
#     [0, 0, 1, 0],
#     [0, 0, 1, 0],
#     [0, 1, 1, 0],
#     [0, 1, 1, 0]
# ]

# c = 0
# for i in range(1,len(a)):
#     if a[c][i] == 1:
#         c = i
    
# for i in range(len(a)):
#     if i != c:
#         if a[i][c] == 1 and a[c][i] == 0:
#             return -1
# else:
#     return c

class Node():
    def __init__(self, info = None):
        self.info = info
        self.l = self.r = None

root = ten = Node(10)
two = Node(-2)
three= Node(3)
four = Node(4)
five = Node(5)
six = Node(6)
ten.l = two
# ten.r = six
two.l = Node(8)
two.r = Node(-4)
# six.l = Node(7)
six.r = Node(5)

m = 0

def maxpath(root, s):
    global m
    if root:
        if m < root.info + s:
            m = root.info + s
        maxpath(root.l, root.info + s)
        maxpath(root.r, root.info + s)

maxpath(root, 0)
print (m)


