class Node():
    def __init__(self, item):
        self.info = item
        self.next = None
k = 4

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)

def fun(node):
    
    if node is None:
        return 1
    x = fun(node.next)
    if (x == k):
        print(node.info)
    return x + 1

fun(head)

