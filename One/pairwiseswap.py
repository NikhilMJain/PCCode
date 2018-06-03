class Node():
    def __init__(self, item):
        self.info = item
        self.next = None

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
# head.next.next.next = Node(4)

def swap(head):
    p = q = head
    newhead = head.next

    while 1:
        q = p.next
        t = q.next
        q.next = p
        if t is None or t.next is None:
            p.next = t
            break
        p.next = t.next
        p = t
    return newhead

x = swap(head)
