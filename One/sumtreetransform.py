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
    

def sumtree(root):
    if root:
        sumtree(root.l)
        sumtree(root.r)
        if root.l is None and root.r is None:
            return

        if root.l is None and root.r is not None:
            root.info += root.r.info
        elif root.r is None and root.l is not None:
            root.info += root.l.info
        elif root.l and root.r:
            root.info += root.info + root.l.info + root.r.info

level(ten)

sumtree(ten)

level(ten)
