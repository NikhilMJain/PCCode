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

ten.l = nine
ten.r = one
nine.l = seven
nine.r = two
seven.l = four
seven.r = three
six.l = three
six.r = five

def ss(root, s):
    if not root:
        return s == 0
    if ss(root.l, s- root.info) or ss(root.r, s-root.info):
        print(root.info)
        return True
    return False

ss(ten, 111)