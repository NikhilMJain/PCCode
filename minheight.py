import math
class Node():
    def __init__(self, info = None):
        self.info = info
        self.l = self.r = None
s = []
s1 = []
head = root = one = Node(1)
two = Node(2)
three= Node(3)
four = Node(4)
five = Node(5)

one.l = two
one.r = four
two.l = three
two.r = five

m = math.inf
def height(root, l):
    global m
    if root:
        if root.l is None and root.r is None:
            m = min(m, l)
            return
        height(root.l, l + 1)
        height(root.r, l + 1)

print(m)
height(root, 0)
print(m)

