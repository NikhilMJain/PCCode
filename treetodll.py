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

prev = None
head = None

def converttodll(root):

    global prev, head
    if root is None:
        return
    converttodll(root.l)
    if prev is not None:
        prev.r = root
        root.l = prev
    else:
        head = root
    prev = root
    converttodll(root.r)

converttodll(one)
