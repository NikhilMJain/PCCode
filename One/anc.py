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

def anc(root, key):
    if root:
        if key == root.info or anc(root.l, key) or anc(root.r, key):
            print(root.info)
            return True
    return False


anc(ten, 4)
print()
anc(ten, 1)