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

def anc(root, key, s ):
    if root:
        if root.info == key:
            s.append(root.info)
            return True
        if anc(root.l, key,s) or anc(root.r, key,s):
            s.append(root.info)
            return True

anc(ten, 4, s)
anc(ten, 9, s1)

print (s, s1)

for i in s:
    if i in s1:
        x = i
        break

print (abs(s.index(x) - s1.index(x)) + 2 if i in s1 and i in s else abs(s.index(x) - s1.index(x)))
