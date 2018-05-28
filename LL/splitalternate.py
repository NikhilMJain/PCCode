class Node():
    def __init__(self, item):
        self.info = item
        self.next = None

f = Node(5)
f.next = Node(6)
f.next.next = Node(9)
f.next.next.next = Node(10)
f.next.next.next.next = Node(12)



def fun(h):
    atail = a = Node('dummy')
    btail = b = Node('dummy')

    flag = True
    cur = h
    while cur:
        if flag:
            atail.next = cur
            atail = atail.next
            flag = not flag
        else:
            btail.next = cur
            btail = btail.next
            flag = not flag
        cur = cur.next
    atail.next = btail.next = None

    return a.next, b.next

x,y = fun(f)

