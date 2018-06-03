class Node():
    def __init__(self, info = None):
        self.info = info
        self.l = self.r = None

one = Node(1)
two = Node(2)
three= Node(3)
four = Node(4)
five = Node(5)

one.l = two
one.r = four
two.l = three
two.r = five


def leftprofile(root):
    if root:
        print root.info
        if root.l:
            leftprofile(root.l)
        elif root.r:
            leftprofile(root.r)

def rightprofile(root):
    if root:
        print root.info
        if root.r:
            rightprofile(root.r)
        elif root.l:
            rightprofile(root.l)   

def leaves(root):
    if root:
        leaves(root.l)
        if not (root.l and root.r):
            print root.info
        leaves(root.r)     

leftprofile(one)
print
rightprofile(one)
leaves(one)