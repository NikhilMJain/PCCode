class Node():
    def __init__(self, item):
        self.info = str(item)
        self.next = None
        
d = {}

head = one = Node(1)
two = Node(2)
three= Node(3)
four = Node(4)
five = Node(5)

one.next = two

two.next = three

three.next = four

four.next = five

five.next = None


tail = None
h = None
k = 2

def rev():
    newhead = None
    global tail, h, k
    while(h):
        x = revlist()
        if newhead is None:
            newhead = x
        else:
            newtail.next = x
        newtail = tail
    return newhead

def revlist():
    global tail, h, k
    newk = k
    cur = None
    tail = h
    while h and newk:
        t = h.next
        h.next = cur
        cur = h
        h = t
        newk -= 1
    return cur

h = head

y = rev()
print(y)