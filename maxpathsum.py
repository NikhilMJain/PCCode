class Node():
    def __init__(self, info = None):
        self.info = info
        self.l = self.r = None
s = []
s1 = []
one = Node(1)
two = Node(2)
three= Node(3)
four = Node(4)
five = Node(5)
six = Node(6)
seven = Node(7)
eight = Node(8)
nine = Node(9)
ten = Node(10)

one.l = two
one.r = three

two.l = Node(4)
two.r = five

three.l = six
three.r = seven

# four.l = three
# four.r = five
#five.l = eight
# three.l = six
# six.l = seven
seven.r = eight
res = 0

def maxpathsum(root, s):
    global res
    if root is None:
        return False
    if root.l is None and root.r is None:
        if root.info + s > res:
            res = root.info + s
    
    maxpathsum(root.l , s + root.info)
    maxpathsum(root.r, s + root.info)

maxpathsum(one, 0)

print(res)