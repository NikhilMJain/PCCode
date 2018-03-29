l = [3,6,1,2,5,4]
class Node():
    def __init__(self, info = None):
        self.info = info
        self.l = self.r = None
s = []
def inorder(head):
    
    cur = head
    while s != [] or cur:

        while cur:
            s.append(cur)
            cur = cur.l
        
        cur = s.pop()
        print cur.info

        cur = cur.r


def insertbst(root):
    root = Node(l[0])
    for i in l[1:]:
        p = Node(i)
        q = root
        while True:
            if p.info < q.info:
                if not q.l:
                    q.l = p
                    break
                else:
                    q = q.l
            else:
                if not q.r:
                    q.r = p
                    break
                else:
                    q = q.r
    return root


key = 41
def search(root):
    if root:
        if key == root.info:
            return root
        elif key < root.info:
            return search(root.l)
        else:
            return search(root.r)
    

root = insertbst(None)
if __name__ == '__main__':
    print search(root)