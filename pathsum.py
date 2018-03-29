class Node():
    def __init__(self, info = None):
        self.info = info
        self.l = self.r = None
s = []
s1 = []
head = one = Node(1)
two = Node(2)
three= Node(3)
four = Node(4)
five = Node(5)
six = Node(6)
seven = Node(7)
one.l = two
two.l = Node(9)
one.r = four
four.l = three
four.r = five
five.r = two
three.l = six
six.l = seven
def sumpath(root, s):
    if root is None:
        return s == 0
    return sumpath(root.l, s - root.info) or sumpath(root.r, s - root.info)
c = 0
def countleaves(root):
    global c
    if root:
        countleaves(root.l)
        if root.l is None and root.r is None:
            c = c + 1
        countleaves(root.r)

def height(root):
    if not root:
        return 0
    return 1 + max(height(root.l), height(root.r))

def diameter(root):
    if root is None:
        return 0
    return max((height(root.l) + height(root.r) + 1), max(diameter(root.l),diameter(root.r)))

# print sumpath(head, 1)
# print sumpath(head, 2)
# print sumpath(head, 3)
# print sumpath(head, 5)
# print sumpath(head, 4)
# print sumpath(head, 6)
# print sumpath(head, 7)
# print sumpath(head, 8)
# print sumpath(head, 9)
# print sumpath(head, 10)
print c
print diameter(head)
countleaves(head)
print c