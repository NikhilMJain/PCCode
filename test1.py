s = []

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
ten = Node(10)
nine = Node(9)

ten.l = nine
ten.r = one
nine.l = seven
nine.r = two
seven.l = four
def level(root):
    

    s.append(root)
    while(s):
        
        cur = s.pop(0)
        print cur.info
        if cur.l:
            s.append(cur.l) 
        if cur.r:
            s.append(cur.r)

def st(root):
    if not root:
        return 0
    x = st(root.l)
    y = st(root.r)
    z = root.info
    root.info = x + y + root.info
    return z

level(ten)

st(ten)

level(ten)
