import searchbst as s

root = s.insertbst(None)



s.key = 4
node = s.search(root)

def delete(root):
    prev = cur = root
    if cur.r is None and cur.l is None:
        del cur
    elif cur.r is not None and cur.l is None:
        cur.info = cur.r.info
        del cur.r
    elif cur.l is not None and cur.r is None:
        cur.info = cur.r.info
        del cur.r
    else:
        p = cur.r
        while p.l:
            p = p.l
        cur.info = p.info
        del p
    return prev

if node:
    s.inorder(root)
    delete(node)

    s.inorder(root)
        


