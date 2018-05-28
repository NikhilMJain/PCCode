import math
class Node():
    def __init__(self, info = None):
        self.info = info
        self.l = self.r = None

ten = Node(10)
two = Node(-2)
three= Node(3)
four = Node(4)
five = Node(5)
root = six = Node(6)
six.l = two
six.r = ten
two.l = Node(8)
# two.r = Node(-4)
# six.l = Node(7)
# six.r = Node(5)

a = []
prev = None
def isBSTinorder(root):
    global prev

    if not root:
        return True

    if not isBSTinorder(root.l):
        return False
    
    if prev and not (root.info > prev.info):
        return False
    
    prev = root

    return isBSTinorder(root.r)

print(isBSTinorder(root))

def isBSTminmax(root, mini, maxi):
    if root is None:
        return True
    
    if mini > root.info or maxi < root.info:
        return False
    
    return isBSTminmax(root.l, mini, root.info) and isBSTminmax(root.r, root.info, maxi)

print(isBSTminmax(root, -math.inf, math.inf))
