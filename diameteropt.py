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
eight = Node(8)
nine = Node(9)
ten = Node(10)
eleven = Node(11)
twelve = Node(12)

one.l = two
one.r = three
two.l = four
two.r = five
three.l = six
three.r = seven
six.r = eight
seven.l = ten
seven.r = nine
ten.r = eleven
eleven.r = twelve

res = 0
def dia(root):
    global res

    if not root:
        return 0
    l = dia(root.l)
    r = dia(root.r)

    res = max(1+l+r, res)

    return l + max(r , 1)
dia(one)
print(res)