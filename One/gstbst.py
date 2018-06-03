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

s = 0
def convert(head):
    global s
    if head:
        convert(head.r)
        s += head.info
        head.info = s
        convert(head.l)

def inord(root):
    if root:
        inord(root.l)
        print root.info
        inord(root.r)




inord(head)
convert(head)
inord(head)