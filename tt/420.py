d = {}
s = []
a = [1, 2, 4, 4, 1, 3, 7, 8, 6, 6]

for i in a:
    if i in d:
        print(i)
        break
    else:
        d[i] = True
#------------------------------
i = 0
st = "This is a sample sentence"
while (i < len(st)):
    while i != len(st) and st[i] != ' ':
        s.append(st[i])
        i += 1
    while s:
        print('{}'.format(s.pop()),end='')
    print(' ',end='')
    i += 1

    

