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
eight = Node(8)
nine = Node(9)
ten = Node(10)
eleven = Node(11)
twelve = Node(12)
thirteen = Node(13)


ten.l = eight
ten.r = two
eight.l = seven
eight.r = six

def fun(root):

    if root is None:
        return True
    
    x = fun(root.l)
    y = fun(root.r)

    if root.l and root.r:
        return (root.info == root.l.info + root.r.info) and x and y
    
    if root.l:
        return (root.info == root.l.info) and x and y
    
    elif root.r:
        return (root.info == root.r.info) and x and y
    
    return (x and y)

#print(fun(ten))


def lca(root, p, q):

    if root is None:
        return
    
    x = lca(root.l, p, q)
    y = lca(root.r, p, q)


    if root.info == p or root.info == q:
        return root

    if x and y:
        return root
    
    elif x:
        return x
    else:
        return y


print(lca(ten,7, 10).info)