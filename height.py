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

one.l = two
one.r = four
two.l = three
two.r = five

def height(root):
    if root is None:
        return 0
    return 1 + max(height(root.l), height(root.r))

def size(root):
    if root is None:
        return 0
    return 1 + size(root.l) + size(root.r)

print size(one)