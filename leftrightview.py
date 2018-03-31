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
three.r = five
maxLevel = 0
def left(root, lev):
    global maxLevel
    if root:
        if lev == maxLevel:
            print root.info
            maxLevel += 1
        left(root.r, lev + 1)
        left(root.l, lev + 1)

left(one, 0)