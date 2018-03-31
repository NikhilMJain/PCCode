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


def verticalpre(root):
    d = {}
    def vt(root, hd):
        if root:
            if hd in d:
                d[hd].append(root.info)
            else:
                d[hd] = [root.info]
            vt(root.l, hd - 1)
            vt(root.r, hd + 1)
    vt(root, 0)
    for i in sorted(d):
        for j in d[i]:
            print j,

def toppre(root):
    d = {}
    def tt(root, hd):
        if root:
            if hd in d:
                d[hd].append(root.info)
            else:
                d[hd] = [root.info]
            tt(root.l, hd - 1)
            tt(root.r, hd + 1)
    tt(root, 0)
    for i in sorted(d):
            print d[i][0],

def verticallevel(root):
    d = {}
    q = []
    def vt(root, hd):
        q.append([root, hd])
        while q:
            cur, h = q.pop(0)
            if h in d:
                d[h].append(cur.info)
            else:
                d[h] = [cur.info]
            if cur.l:
                q.append([cur.l, h - 1])
            if cur.r:
                q.append([cur.r, h + 1])
    vt(root, 0)
    for i in sorted(d):
        for j in d[i]:
            print j, 


def toplevel(root):
    d = {}
    q = []
    def tt(root, hd):
        q.append([root, hd])
        while q:
            cur, h = q.pop(0)
            if h in d:
                d[h].append(cur.info)
            else:
                d[h] = [cur.info]
            if cur.l:
                q.append([cur.l, h - 1])
            if cur.r:
                q.append([cur.r, h + 1])
    tt(root, 0)
    for i in sorted(d):
        print d[i][0], 

verticalpre(one)
print
verticallevel(one)
print
toplevel(one)
print
toppre(one)