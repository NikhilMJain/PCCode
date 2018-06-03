class Node():
    def __init__(self, info = None):
        self.info = info
        self.l = self.r = None

root = one = Node(1)
two = Node(2)
three= Node(3)
four = Node(4)
five = Node(5)

one.l = two
one.r = four
two.l = three
two.r = five

#post and swap
def mirror(root):
    if root:
        mirror(root.l)
        mirror(root.r)
        root.l,root.r = root.r,root.l

def preorder(root):
    if root:
        print root.info
        preorder(root.l)
        preorder(root.r)

preorder(root)
print
mirror(root)
print
preorder(root)