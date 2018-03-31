class Node():
    def __init__(self, item):
        self.info = item
        self.next = None

def sumlist(f, s):
    head = None
    c = 0
    while f or s:
        sum = (f.info if f else 0) + (s.info if s else 0)
        sum = sum + 1 if c else sum
        if sum > 9:
            sum = sum % 10
            c = 1
        else:
            c = 0
        
        t = Node(sum)
        if head is None:
            head = cur = t
        else:
            cur.next = t
            cur = t
        f = f.next if f else f
        s = s.next if s else s
    if c:
        cur.next = Node(1)
    return head

f = Node(5)
f.next = Node(6)
f.next.next = Node(3)

s = Node(8)



x = sumlist(f, s)
