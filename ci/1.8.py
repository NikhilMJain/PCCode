s1 = 'waterbottle'
s2 = 'bottlewater'

import queue

def isSS(s1,s2):
    i = 0
    l = len(s1)
    
    for i in range(l):
        for j in range(l):
            if s1[j] == s2[(i+j)%l]:
                if j == l - 1:
                    print("Yes")
            else:
                break


isSS(list(s1),list(s2))

