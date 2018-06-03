class Node():
    def __init__(self, item):
        self.info = item
        self.next = None
        
res = None

def ms(h):
    global res

    if h is None or h.next is None:
        return

    x, y = spl(h)

    x = ms(x)
    y = ms(y)

    res = sm(x, y)

def sm(f, s):
    global res
    

    if f is None:
        return s
    elif s is None:
        return f


    if f.info < s.info:
        node = f
        node.next = sm(f.next, s)
    else:
        node = s
        node.next = sm(f, s.next)

    return node

def spl(h):
    if h is None:
        return (None, None)
    if h.next is None:
        return (h, None)
    slow = h
    fast = slow.next

    while fast:
        fast = fast.next
        if fast:
            slow = slow.next
            fast = fast.next
    
    fp = h
    sp = slow.next
    slow.next = None

    return (fp, sp)

head = Node(7)
head.next = Node(4)
head.next.next = Node(2)

      
x = ms(head)



