class Node():
    def __init__(self, item):
        self.info = item
        self.next = None

f = Node(12)
f.next = Node(1)
f.next.next = Node(9)
f.next.next.next = Node(10)
f.next.next.next.next = Node(112)

def fun(h):
    if h is None:
        return
    fun(h.next)
    print(h.info)

fun(f)