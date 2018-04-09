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
ten = Node(10)
nine = Node(9)

# ten.l = nine
# ten.r = one
# nine.l = seven
# nine.r = two
# seven.l = four
# seven.r = three

root = Node(6)
root.l = Node(2)
root.l.l = Node(-8)
root.r = Node(14)
root.r.l = Node(13)
root.r.r = Node(15)
root.r.l.l = Node(7)




prev = head = None
def con(root):
    global prev, head
    if root is None:
        return
    con(root.l)

    node = Node(root.info)
    if head == None:
        head = prev = node
    else:
        prev.r = node
        node.l = prev
        prev = node
    
    con(root.r)

def isPresent(l, r, key):
    while l != r:
        if (l.info + r.info) == key:
            return True
        if l.info + r.info < key:
            l = l.r
        else:
            r = r.l
    return False

# con(root)

# tail = prev
# cur = head
# while cur is not None and cur.info < 0:
#     if isPresent(cur.r, tail, -cur.info):
#         print True
#         break
#     else:
#         cur = cur.r
# else:
#     print False

