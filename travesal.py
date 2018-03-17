s = []
class Node():
    def __init__(self, item):
        self.info = item
        self.r = self.l = None

head = None

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

postorder()

