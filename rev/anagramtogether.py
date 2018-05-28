s = ['act', 'ant', 'cat', 'nat']
i = [0,1,2,3]
print(s)
for c in range(len(s)):
    s[c] = ''.join(sorted(s[c]))
print(s)

zipped = list(zip(s, i))

print(zipped)

#incomplete