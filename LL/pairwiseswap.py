class Node():
    def __init__(self, item):
        self.info = item
        self.next = None

f = Node(1)
f.next = Node(3)
f.next.next = Node(6)
f.next.next.next = Node(10)
f.next.next.next.next = Node(5)

def fun(h):
    cur = h

    while cur and cur.next:
        cur.next.info, cur.info = cur.info , cur.next.info
        cur = cur.next.next
    return h

x = fun(f)
