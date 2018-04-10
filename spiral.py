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
seven.r = six

s1 = []
s2 = []

def spiral(root):
    s1.append(root)

    while s1 or s2:

        while s1:
            cur = s1.pop()
            print(cur.info)
            if cur.l:
                s2.append(cur.r)
            if cur.r:
                s2.append(cur.l)
        while s2:
            cur = s2.pop()
            print(cur.info)
            if cur.l:
                s1.append(cur.l)
            if cur.r:
                s1.append(cur.r)

spiral(ten)