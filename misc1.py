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

def leafsum(root, key):

    if root is None:
        return key == 0
    
    return leafsum(root.l, key - root.info) or leafsum(root.r, key - root.info)

print leafsum(ten, 22)