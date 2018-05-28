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
