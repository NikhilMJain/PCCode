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

def boundary(root):
    if root:
        print root.info
    left(root.l)
    leaves(root.l)
    leaves(root.r)
    right(root.r)

def left(root):
    if root:
        
        if root.l:
            print root.info
            left(root.l)
        elif(root.r):
            print root.info
            right(root.r)

def leaves(root):
    if root:
        if root.l:
            leaves(root.l)
        if root.l is None and root.r is None:
            print root.info
        if root.r:
            leaves(root.r)

def right(root):
    if root:
        if root.r:
            right(root.r)
            print root.info
        elif root.l:
            right(root.l)
            print root.info
        


boundary(head)
        