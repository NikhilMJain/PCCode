class Node:
    def __init__(self, val = None):
        self.ref = {}
        self.char = val
        self.isWord = False
        self.count = 0
    
def add(root, word):
    cur = root
    for char in word:
        if char in cur.ref:
            cur.ref[char].count += 1
        else:
            node = Node(char)
            cur.ref[char] = node
            cur.ref[char].count += 1
        cur = cur.ref[char]
    cur.isWord = True


def prefix(root, text):
    cur = root
    if not cur.ref:
        return None
    for i in text:
        if i in cur.ref:
            cur = cur.ref[i]
        else:
            return None
    return cur.count

root = Node()

add(root, 'abc')
add(root, 'and')

add(root, "hackathon")
add(root, 'hack')

print(prefix(root, 'hac'))
print(prefix(root, 'hack'))
print(prefix(root, 'hackathon'))
print(prefix(root, 'ha'))
print(prefix(root, 'hammer'))


