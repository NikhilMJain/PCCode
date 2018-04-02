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
# two.l = four
# two.r = five
# three.l = six
# three.r = seven
# six.r = eight
# seven.l = ten
# seven.r = nine
# ten.r = eleven
# eleven.r = twelve
mind = 0
maxd = 0
def diameter(root):


    def d(root, hd):
        global mind, maxd
        if root:
            mind = min(mind, hd)
            maxd = max(maxd, hd)
            d(root.l, hd - 1)
            d(root.r, hd + 1)

    d(root, 0)
    return abs(maxd) + abs(mind) + 1


print diameter(one)