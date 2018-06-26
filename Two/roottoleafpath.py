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


ten.l = eight
ten.r = two
eight.l = seven
eight.r = six


q = []

def fun(root):
    if root is None:
        return
    q.append(root.info)

    fun(root.l)
    if root.l is None and root.r is None:
        print(q)
    fun(root.r)
    
    q.pop()

fun(ten)
