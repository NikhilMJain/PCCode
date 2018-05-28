class Node():
    def __init__(self, item):
        self.info = item
        self.next = None

f = Node(5)
f.next = Node(6)
f.next.next = Node(6)
f.next.next.next = Node(10)
f.next.next.next.next = Node(12)

def fun(h):
    cur = h
    while cur:
        while cur.next and cur.info == cur.next.info:
            cur.next = cur.next.next
            cur = cur.next
        cur = cur.next
    return h

x = fun(f) 