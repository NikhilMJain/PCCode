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
thirteen = Node(13)

# one.l = two
# one.r = three
# two.l = four
# two.r = five
# four.l = six
# four.r = seven
# seven.l = nine
# nine.r = twelve
# five.r = eight
# eight.l = ten
# eight.r = eleven
# ten.r = eleven
# eleven.l = thirteen
# eleven.r = Node(15)
############################
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

reqx = reqy = reqnode = 0
res = 0
def dia(root):

    global res, reqnode, reqx, reqy

    if not root:
        return 0
    l = dia(root.l)
    r = dia(root.r)

    if res < 1 + l + r:
        reqx = l
        reqy = r
        reqnode = root

    res = max(1+l+r, res)

    return 1 + max(r , l)

def printleaves(root, lev):
    if root is None:
        return
    if lev == 0:
        print(root.info)

    printleaves(root.l, lev - 1)
    printleaves(root.r, lev - 1)

dia(one)
printleaves(reqnode.l, reqx - 1)
print()
printleaves(reqnode.r, reqy - 1)
