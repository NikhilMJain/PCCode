class Node():
    def __init__(self, info = None):
        self.info = info
        self.l = self.r = None
s = []
s1 = []
head = one = root = Node(1)
two = Node(2)
three= Node(3)
four = Node(4)
five = Node(5)

one.l = two
one.r = four
two.l = three
two.r = five

l = []
def inorder(root):
    if root:
        inorder(root.l)
        l.append(root.info)
        inorder(root.r)

def pri(root):
    if root:
        pri(root.l)
        print root.info
        pri(root.r)

def convert(root):
    
    if root:
        convert(root.l)
        root.info = l.pop(0)
        convert(root.r)

pri(root)
inorder(root)
l.sort()
convert(root)

pri(root)