s = ['a','n','a']
distinct = set()
def an(l, r):
    if l == r:
        distinct.add(''.join(s))
    else:
        for i in range(l, r + 1):
            s[l], s[i] = s[i], s[l]
            an(l+1, r)
            s[l], s[i] = s[i], s[l]

an(0, 2)
print(distinct)