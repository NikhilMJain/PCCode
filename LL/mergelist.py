class Node():
    def __init__(self, item):
        self.info = item
        self.next = None

f = Node(5)
f.next = Node(6)
f.next.next = Node(9)
f.next.next.next = Node(10)
f.next.next.next.next = Node(12)

s = Node(1)
s.next = Node(2)
s.next.next = Node(3)
s.next.next.next = Node(11)
s.next.next.next.next = Node(13)

def fun(a, b):

    if not a:
        return b
    if not b:
        return a
    
    if a.info < b.info:
        node = a
        node.next = fun(a.next, b)
    else:
        node = b
        node.next = fun(a, b.next)
    
    return node

x = fun(f, s)
print(x)