# a = [3, 3, 4, 2, 4, 4, 2, 4, 4]

# i = 0
# c = 0
# cd = a[i]
# for i in range(len(a)):
#     if cd == a[i]:
#         c += 1
#     else:
#         c -= 1
#     if c == 0:
#         cd = a[i]
#         c = 1

# print cd

class Node():
    def __init__(self, info = None):
        self.info = info
        self.l = self.r = None

def sumtree(root):
    if root is None:
        return 0
    ls = sumtree(root.l)
    rs = sumtree(root.r)

    old = root.info
    root.info = ls + rs
    return old + root.info


def inorder(root):
    if root:
        inorder(root.l)
        print root.info,
        inorder(root.r)

root = ten = Node(10)
two = Node(-2)
three= Node(3)
four = Node(4)
five = Node(5)
six = Node(6)
ten.l = two
ten.r = six
two.l = Node(8)
two.r = Node(-4)
six.l = Node(7)
six.r = Node(5)

inorder(root)
print
sumtree(root)
inorder(root)



