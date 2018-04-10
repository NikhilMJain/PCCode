# a = ['d','i','n','c','h','a','k']
# print(a)
# i = 0
# j = len(a) - 1
# while i != j:
#     a[i] = chr(ord(a[i]) ^ ord(a[j]))
#     a[j] = chr(ord(a[i]) ^ ord(a[j]))
#     a[i] = chr(ord(a[i]) ^ ord(a[j]))
#     i += 1
#     j -= 1
# print(a)

a = [1,2,2,3]
res = 0
c = 0
for i in a:
    res = res + i
for i in range(len(a)):
    c = c + a[i]
    res = res - a[i]
    if c == res:
        print(i)
