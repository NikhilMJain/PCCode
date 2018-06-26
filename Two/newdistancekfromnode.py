#print above confused... abandoned
class Node():
    def __init__(self, info = None):
        self.info = info
        self.l = self.r = None
        
head = one = Node(1)
two = Node(2)
three= Node(3)
four = Node(4)
five = Node(5)
six = Node(6)
seven = Node(7)
eight = Node(8)
ten = Node(10)
nine = Node(9)

one.l = two
one.r = three
two.l = four
two.r = five
three.l = six
three.r = seven
six.l = eight
eight.l = nine


s = []
node = None

def find_target(root, target):
    global node
    if root is None:
        return False

    if root.info == target:
        s.append(root)
        node = root
        return True

    x = find_target(root.l, target)
    y = find_target(root.r, target)

    if x or y:
        s.append(root)
        return True
    return False

def print_above(root, i, k, l):

    if root is None:
        return
    if i == k:
        print(root.info)
    elif root.l == s[i - 1]:
        print_down(root.r, (k - i) - 1)
    else:
        print_down(root.l, (k - i) - 1)

def print_down(root, l):
    if root is None:
        return 
    
    if l == 0:
        print(root.info)
    
    print_down(root.l, l - 1)
    print_down(root.r, l - 1)


def dist(root, target, k):
    global node
    find_target(root, target)

    print_down(node, k)

    for i in range(1, len(s)):
        print_above(s[i], i, k, l)


dist(one, 6, 3)