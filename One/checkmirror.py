class Node():
    def __init__(self, info = None):
        self.info = info
        self.l = self.r = None
        
def checkMirror(f,s):
    if f is None and s is None:
        return True
    if (f is None and s is not None) or (f is not None and s is None):
        return False
    if f.info == s.info:
        return checkMirror(f.l, s.r) and checkMirror(f.r, s.l)
    return False

one = Node(1)
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

newone.l = newfour
newone.r = newtwo
newtwo.l = newfive
newtwo.r = newthree
newthree.l = Node(44)

print checkMirror(one, newone)