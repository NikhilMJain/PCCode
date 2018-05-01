a = 'abc'


def Unique(a):
    c = 0
    for i in a:
        if c & (1 << (ord(i) - ord('a'))):
            return False
        c = c | (1 << (ord(i) - ord('a')))
    return True

print(Unique(a))