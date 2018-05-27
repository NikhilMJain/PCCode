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


def rev(h):

    cur = None
    while h:
        t = h.next
        h.next = cur
        cur = h
        h = t
    return cur


def fun(h):
    cur = h

    cur = h = rev(h)
    maxx = 0
    #cur = cur.next
    prev = None

    while cur:
        if cur.info > maxx:
            maxx = cur.info
            prev = cur
            cur = cur.next
        else:
            prev.next = cur.next
            cur = cur.next

    return rev(h)

x = fun(f)