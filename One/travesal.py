s = []
class Node():
    def __init__(self, item):
        self.info = item
        self.r = self.l = None

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
one.l = four
one.r = three


def level(root):
    width = 1

    s.append(root)
    while(s):
        width = max(width, len(s))
        cur = s.pop(0)
        
        if cur.l:
            s.append(cur.l) 
        if cur.r:
            s.append(cur.r)
    return width



def preorder():
    global head
    s.append(head)
    while s != []:
        x = s.pop()
        print x.info
        if x.r:
            s.append(x.r)
        if x.l:
            s.append(x.l)

def inorder():
    global head
    cur = head
    while s != [] or cur:

        while cur:
            s.append(cur)
            cur = cur.l
        
        cur = s.pop()
        print cur.info

        cur = cur.r

s2 = []
def postorder():
    global head

    s.append(head)
    while(s):
        x = s.pop()
        s2.append(x)

        if x.l:
            s.append(x.l)
        if x.r:
            s.append(x.r)
    while s2:
        print s2.pop().info

#create
head = Node('A')
B = Node('B')
C = Node('C')
D = Node('D')
E = Node('E')
head.l = B
head.r = C
C.l = D
C.r = E

print level(ten)


