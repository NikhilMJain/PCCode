s = 'okay so this is the sentence '
s = list(s)

l = len(s)
t = []
j = 0
for i in range(l):
    if s[i] != ' ':
        t.append(s[i])
    else:
        for _ in '%20':
            t.append(_)

print(''.join(t))



