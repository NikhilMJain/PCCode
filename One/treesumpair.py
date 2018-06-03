class Node():
    def __init__(self, info = None):
        self.info = info
        self.l = self.r = None
        
def fun(root, s):
    s1 = []
    s2 = []
    fd = sd = True
    cur1 = cur2 = root

    while True:
        while fd and (cur1 or s1):
            while cur1:
                s1.append(cur1)
                cur1 = cur1.l
            
            cur1 = s1.pop()
            node1 = cur1
            fd = False

            cur1 = cur1.r

        while sd and (cur2 or s2):
            while cur2:
                s2.append(cur2)
                cur2 = cur2.r
            
            cur2 = s2.pop()
            node2 = cur2
            sd = False

            cur2 = cur2.l
        
        if node1.info > node2.info:
            break

        if node1.info + node2.info == s:
            print((node1.info, node2.info))
        if node1.info + node2.info < s:
            fd = True
        else:
            sd = True
        


# head = one = Node(1)
# two = Node(2)
# three= Node(3)
# four = Node(4)
# five = Node(5)
# six = Node(6)
# seven = Node(7)
# eight = Node(8)
# ten = Node(10)
# nine = Node(9)

# six.l = four
# four.l = three
# four.r= five
# six.r = eight
# eight.l = seven
# eight.r = nine

root =  Node(15)
root.l = Node(10)
root.r = Node(20)
root.l.l = Node(8)
root.l.r = Node(12)
root.r.l = Node(16)
root.r.r = Node(25)

fun(root, 33)