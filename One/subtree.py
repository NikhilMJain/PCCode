def isIdentical(f, s):
    if f is None and s is None:
        return True
    if (f is None and s is not None) or (f is not None and s is None):
        return False
    if f.info == s.info:
        return isIdentical(f.l, s.l) and isIdentical(f.r, s.r)
    return False
    

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

one.l = two
one.r = four
two.l = three
two.r = five

newone = Node(1)
newtwo = Node(2)
newthree= Node(3)
newfour = Node(4)
newfive = Node(5)

newone.l = newtwo
newone.r = newfour
newtwo.l = newthree
newtwo.r = None

def search(f, s):
    global found
    if f:
        if f.info == s:
            found = f
        search(f.l, s)
        search(f.r, s)
    

n = search(one, newtwo.info)
print isIdentical(found, newtwo)