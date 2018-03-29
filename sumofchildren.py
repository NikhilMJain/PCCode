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
ten = Node(10)
nine = Node(9)

ten.l = nine
ten.r = one
nine.l = seven
nine.r = two
seven.l = four
seven.r = three
# six.l = three
# six.r = five

# ten.l = six
# ten.r = four
# four.l = three
# four.r = one
# six. l = two
# six.r = Node(5)
# one.l = two
# two.l = Node(9)
# one.r = four
# four.l = three
# four.r = five
# five.r = two
# three.l = six
# six.l = seven

def sumofchildren(root):
    if root:
        lc = sumofchildren(root.l)
        rc = sumofchildren(root.r)
        if root.l is None and root.r is None:
            return True
        elif root.l is None and root.r is not None:
            return root.info == root.r.info and rc
        elif root.l is not None and root.r is None:
            return root.info == root.l.info and lc
        else:
            return root.info == (root.l.info + root.r.info) and rc and lc

print sumofchildren(ten)