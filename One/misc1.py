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

def leafsum(root, key):

    if root is None:
        return key == 0
    
    return leafsum(root.l, key - root.info) or leafsum(root.r, key - root.info)

def getlevel(root, target, level):
    if root:
        if root.info == target:
            return level
        x = getlevel(root.l, target, level + 1)
        if x != 0:
            return x
        else:
            return getlevel(root.r, target, level + 1)
    return 0
print getlevel(ten, 10,1)
print getlevel(ten, 1,1)
print getlevel(ten, 7,1)
print getlevel(ten, 2,1)
print getlevel(ten, 3,1)
    

#print leafsum(ten, 22)

