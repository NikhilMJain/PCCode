class Node():
    def __init__(self, info = None):
        self.info = info
        self.l = self.r = None
s = []
s1 = []
one = Node(1)
two = Node(2)
three= Node(3)
four = Node(4)
five = Node(5)
six = Node(6)
seven = Node(7)
eight = Node(8)
nine = Node(9)
ten = Node(10)
minusfive = Node(-5)
minusthree = Node(-3)
res = 0

one.l = two
two.l = four
two.r = minusfive
minusfive.l = eight
one.r = minusthree
minusthree.l = six
minusthree.r = seven



def fun(root):
    global res

    if root is None:
        return 0

    x = fun(root.l)
    y = fun(root.r)

    c = x + y + root.info

    if c > res:
        res = c
    
    return max(x, y) + root.info

fun(one)
print(res)