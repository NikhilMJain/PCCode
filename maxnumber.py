import functools
c = 0
def myKey(a, b):
    global c
    c += 1

    ab = int(str(a) + str(b))
    ba = int(str(b) + str(a))
    print(ab,ba,ab-ba)
    return ab - ba


a = [1, 34, 3, 98, 9, 76, 45, 4]
a = [str(i) for i in a]
a = sorted(a,key=functools.cmp_to_key(myKey),reverse=True)
print(''.join((a)))
print(c)