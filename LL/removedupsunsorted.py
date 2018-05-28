class Node():
    def __init__(self, item):
        self.info = item
        self.next = None

f = Node(5)
f.next = Node(6)
f.next.next = Node(6)
f.next.next.next = Node(10)
f.next.next.next.next = Node(5)

d = {}

def fun(h):
    prev = None
    cur = h
    while cur:
        if cur.info in d:
            if prev:
                prev.next = cur.next
            
        else:
            d[cur.info] = True
            prev = cur
        cur = cur.next        
    return h

    
x = fun(f)