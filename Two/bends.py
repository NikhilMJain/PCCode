
class Node():
    def __init__(self, info = None):
        self.info = info
        self.l = self.r = None

count = 0

# head = one = Node(1)
# two = Node(2)
# three= Node(3)
# four = Node(4)
# five = Node(5)
# six = Node(6)
# seven = Node(7)
# eight = Node(8)
# ten = Node(10)
# nine = Node(9)

# one.l = two
# one.r = three
# two.l = four
# two.r = five
# three.l = six
# three.r = seven
# six.l = eight
# eight.r = nine
root = Node(10)
root.l = Node(8)
root.r = Node(2)
root.l.l = Node(3)
root.l.r = Node(5)
root.r.l = Node(2)
root.r.l.r = Node(1)
root.r.l.r.l = Node(9)


node = None
def fun(root, dir, c):
    global count, node

    if root is None:
        return
    
    if c > count:
        node = root
        count = c

    if dir == -1:
        fun(root.l, 0, 1)
        fun(root.r, 1, 1)
    elif dir == 0:
        fun(root.l, 0, c)
        fun(root.r, 1, c + 1)
    else:
        fun(root.l, 0, c + 1)
        fun(root.r, 1, c)

fun(root, -1, 0)
print(count, node.info)