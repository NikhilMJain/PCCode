s = bytearray(['Y', 'o', 'l', 'o'])
print s
i = 0
j = 3

while i < j:
    # s[i] = chr(ord(s[i]) ^ ord(s[j]))
    # s[j] = chr(ord(s[j]) ^ ord(s[i]))
    # s[i] = chr(ord(s[i]) ^ ord(s[j]))

    s[i] ^= s[j]
    s[j] ^= s[i]
    s[i] ^= s[j]

    i += 1
    j -= 1

print s
print ''.join(s)