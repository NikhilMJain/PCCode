class Node():
    def __init__(self, item):
        self.info = str(item)
        self.next = None
        self.arbit = None
d = {}

head = one = Node(1)
two = Node(2)
three= Node(3)
four = Node(4)
five = Node(5)

one.next = two
one.arbit = four
two.next = three
two.arbit = one
three.next = four
three.arbit = five
four.next = five
four.arbit = three
five.next = None
five.arbit = two

del  head, cur, one
cur = head
while cur:
    node = Node(cur.info)
    d[id(cur)] = [cur, node]
    cur = cur.next

for i in d:
    if d[i]:
        d[i][1].next = d[id(d[i][0].next)][1] if d[i][0].next else None
        d[i][1].arbit = d[id(d[i][0].arbit)][1] if d[i][0].arbit else None

newHead = d[id(head)][1]
print 'Done'

cur = head
newCur = newHead
while cur:
    print(cur.info + ':' +newCur.info + '::' + cur.next.info +':'+newCur.next.info+'::' +cur.arbit.info +':'+newCur.arbit.info ),
    cur = cur.next
    newCur = newCur.next

