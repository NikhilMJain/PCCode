a = ['a','b','c','d','e',None]

def rev(a):
    i = 0
    c = 0
    while a[i] != None:
        i+=1
        c+=1
    i = 0
    while i < c//2:
        a[i],a[c-1-i] = a[c-1-i],a[i]
        i += 1

    print(a)
    #print("".join(a))

rev(a) 