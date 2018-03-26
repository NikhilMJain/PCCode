class Node():
    def __init__(self, info = None):
        self.info = info
        self.l = self.r = None
s = []
s1 = []
head = one = Node(1)
two = Node(2)
three= Node(3)
four = Node(4)
five = Node(5)

one.l = two
one.r = four
two.l = three
two.r = five


root = Node()    

def preorder(root):
    s.append(root)
    while s:
        cur = s.pop()
        print cur.info

        if cur.l:
            s.append(cur.r)
        if cur.r:
            s.append(cur.l)
    
def inorder(root):
    
    cur = root
    

    while s or cur:
        
        while cur:
            s.append(cur)
            cur = cur.l  
        cur = s.pop()
        if not cur.l and not cur.r:
            print cur.info
        cur = cur.r


# # def postorder(root):
# #     cur = root
# #     s.append(root)
# #     while s:
# #         cur = s.pop()
# #         s1.append(cur)
# #         if cur.l:
# #             s.append(cur.l)
# #         if cur.r:
# #             s.append(cur.r)
        
# #     while s1:
# #         print s1.pop().info
# # flip = False    
# c = True    
# def level(root, lev):
#     global c

#     if root is None:
#         return
#     if lev == 1 and c:
#         print root.info
#         c = False
#         return
        
#     else:
#         # if flip:
#         #     level(root.l, lev - 1)
#         #     level(root.r, lev - 1)
#         # else:
#         #     level(root.r, lev - 1)
#         #     level(root.l, lev - 1)
#         level(root.l, lev - 1)
#         level(root.r, lev - 1)
# for _ in range(1,4):
#     level(head, _)
#     c = True
#     #flip = not flip
#     print 

# postorder(head)
# def vertical(root, hd):
#     l = []


#     while s:
#         hdl = hdl - 1
#         hdr = hdr + 1
#         cur = s.pop(0)
#         if cur.l:

#         s.append(cur.l)
        


# def deleteTree(node):
#     if node is None:
#         return None
#     deleteTree(node.l)
#     deleteTree(node.r)
#     print node.info
#     del node

i = 0
# deleteTree(head)
def levelNone(root):
    stop = False
    cur = head
    s.append(cur)
    s.append(None)
    i = 0
    while s:
        
        cur = s[i]
        i += 1
        if cur:
            stop = False
            print cur.info
            if cur.l:
                s.append(cur.l)
            if cur.r:
                s.append(cur.r)
        else:
            if stop:
                return

            stop = True
            print
            s.append(None)
    

# def leafprint(root):
#     cur = root
#     s = []
#     p = False

#     while s or cur:
        
#         while cur:
#             s.append(cur)
#             cur = cur.l  
#         cur = s.pop()
#         if not cur.l and not cur.r: and p:
#             print cur.info
#         p = True
#         cur = cur.r




levelNone(head)
i = 0
while s[i] or s[i+1]: 
    if s[i+1] == None:
        print s[i].info
    i+=1


leafprint(root)

d = {}

