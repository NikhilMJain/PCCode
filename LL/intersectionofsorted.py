class Node():
    def __init__(self, item):
        self.info = item
        self.next = None

f = Node(12)
f.next = Node(15)
f.next.next = Node(10)
f.next.next.next = Node(11)
f.next.next.next.next = Node(5)
f.next.next.next.next.next = Node(6)
f.next.next.next.next.next.next = Node(2)
f.next.next.next.next.next.next.next = Node(3)

s = Node(1)
s.next = Node(2)
s.next.next = Node(9)
s.next.next.next = Node(12)
s.next.next.next.next = Node(13)

def fun(a, b):

    res = cur = Node('yo')

    while a and b:
        if a.info == b.info:
            res.next = Node(a.info)
            res = res.next
            a = a.next
            b = b.next

        elif a.info < b.info:
            a = a.next
        else:
            b = b.next
    return cur.next

x = fun(f, s)