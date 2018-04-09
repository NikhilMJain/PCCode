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
# nine.l = seven
# nine.r = two
# seven.l = four
# seven.r = three
# two.r = five
# five.r = six
def pathsum(root, s):
    if root:
        if root.l is None and root.r is None:
            if root.info == s:
                print(root.info)
                return True
            
        if pathsum(root.l, s - root.info) or pathsum(root.r, s - root.info):
            print(root.info)
            return True
    return False

#def diameter(root):

def height(root):
    if root:
        return 1 + max (height(root.l),height(root.r))
    else:
        return 0

def diameter(root):
    if root:
        return max(height(root.l) + height(root.r) + 1, max(diameter(root.l), diameter(root.r))) 
    return 0
#pathsum(ten, 219)

def size(root):
    if root:
        return 1 + size(root.l) + size(root.r)
    return 0
#print (size(ten))

head = prev = None

def treetodll(root):
    global head, prev
    if root is None:
        return
    treetodll(root.l)
    node = Node(root.info)
    if head is None:
        head = node
        prev = head
    else:
        prev.r = node
        node.l = prev
        prev = node
    treetodll(root.r)
pf = []
ps = []
def lowestancestor(f, s):
    
    def path(root, key):
        if root is None:
            return False
        if root.info == key:
            x.append(root.info)
            return True
        if path(root.l, key) or path(root.r, key):
            x.append(root.info)
            return True
    x = pf
    path(ten, 1)
    x = ps
    path(ten, 10)
    for i in pf:
        if i in ps:
            print i
            break

def left(root):
    if root:
        if root.l:
            print root.info
            left(root.l)
        elif root.r:
            print root.info
            left(root.r)


def right(root):
    if root:
        if root.l:
            print root.info
            right(root.r)
        elif root.r:
            print root.info
            right(root.l)

def leaf(root):
    if root:
        if root.l:
            leaf(root.l)
        if not root.l and not root.r:
            print root.info
        if root.r:
            leaf(root.r)

    
def boundary(root):
    if root:
        print root.info
        left(root.l)
        leaf(root.l)
        leaf(root.r)
        right(root.r)

# # boundary(ten)
# lowestancestor(four, one)
s = []
# def chain(root):
#     s.append(root)
#     s.append(None)
#     while s and s[-1] is not None and s[-2] is not None:
#         while s[0] is not None:
            
def isMirror(f, s):
    if f and s:
        
        if f is None and s is None:
            return True
        if f.l is None and s.r is None:
            return True
        if f.r is None and s.l is None:
            return True
        if f.l and f.r and s.l and s.r:
            return isMirror(f.l, s.r) and isMirror(f.r, s.l)
    return False

print isMirror(ten, ten)
