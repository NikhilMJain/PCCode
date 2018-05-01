s = 'abccb5'

s = list(s)
l = len(s)
t = 0
for i in range(l):
    for j in range(0, i):
        if s[i] == s[j]:
            break
    else:
        s[t] = s[i]
        t += 1
s = s[:t]
print(''.join(s))
    

