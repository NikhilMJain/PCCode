class Node():
    def __init__(self, item):
        self.info = item
        self.next = None

f = Node(5)
f.next = Node(6)
f.next.next = Node(3)
f.next.next.next = Node(6)
f.next.next.next.next = Node(5)

cur = f
def fun(h):
    global cur
    if not h:
        return True
    isP = fun(h.next)
    if isP and cur.info == h.info:
        cur = cur.next
        return True
    return False

print(fun(f))