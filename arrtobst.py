class Node():
    def __init__(self, info = None):
        self.info = info
        self.l = self.r = None

a = [1,2,3,4,5,6,7,8,9,10]

def atobst(l, r):
    if l <= r:

        m = (l + r) // 2
        root = Node(a[m])

        root.l = atobst(l, m - 1)
        root.r = atobst(m + 1, r)
        return root
    return None

root = atobst(0, len(a) - 1)
print