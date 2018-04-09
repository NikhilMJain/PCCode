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
f = 0
def zig(root):
    f = 0
    s.append(root)
    while s:
        cur = s.pop(0)
        print(cur.info)
        if f:
            if cur.l:
                s.append(cur.l)
            if cur.r:
                s.append(cur.r)
            f = 0
        else:
            if cur.r:
                s.append(cur.r)
            if cur.l:
                s.append(cur.l)
            f = 1

zig(ten)