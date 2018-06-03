s = []
class Node():
    def __init__(self, item):
        self.info = item
        self.r = self.l = None


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
one.l = four
# one.r = three

def isFoldable(root, mroot):
    if root or mroot:
        if root.l and mroot.r:
            return True
        if root.r and mroot.l:
            return True
        if root.l and not mroot.r:
            return False
        if root.r and not mroot.l:
            return False
        return isFoldable(root.l, mroot.r) and isFoldable(root.r, mroot.l)
    if root is None and mroot is None:
        return True
    return False


print isFoldable(ten,ten)
