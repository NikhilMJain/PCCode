class Node():
    def __init__(self, info = None):
        self.info = info
        self.l = self.r = None

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
ten.l = nine
ten.r = one
nine.l = seven
nine.r = two
one.l = four
one.r = three

def mir(f, s):
    
    if not f and not s:
        return True
    if f and s:
        x = mir(f.l, s.r)
        y = mir(f.r, s.l)
    if (f.l and s.r) or (f.r and s.l) or(f.l and s.r and f.r and s.l):
        return True
    return x and y

print(mir(ten,nine))
    