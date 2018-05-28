s = []
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



one.l = two
one.r = three
two.l = four
two.r = five
three.l = six
three.r = seven
six.r = eight
seven.l = ten
seven.r = nine
ten.r = eleven
eleven.r = twelve
f = True
tl = 0
tn = None

def dist(root, t, d):
    global tl, tn, f

    
    def findt(root, t, lev):
        global tl, tn, f
        if root:
            x = findt(root.l, t, lev + 1)
            y = findt(root.r, t, lev + 1)
            if x or y:
                s.append(root)
                return True
            if root.info == t:
                tl = lev
                tn = root
                return True
        return False 
            
    
    findt(root, t, 0)

    def printbelow(root, lev):
        global tl, tn
        if root:
            printbelow(root.l, lev - 1)
            if lev == 0:
                print(root.info, end=' ') 
            printbelow(root.r, lev - 1)
    
    printbelow(tn, d)
    
    def printabove(root, k):
        while s:
            x = s.pop()
            printbelow(x, len(s))
    printabove(root, 2)    


        
x = 0
dist(one, 7, 2)
