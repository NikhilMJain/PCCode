a = [3,4,6,5,1,2]

ss = fs = 20000
sl = fl = 0

for i in a:
    if ss > i:
        if fs > i:
            ss =fs
            fs = i
        else:
            ss = i
    
    if sl < i:
        if fl < i:
            sl =fl
            fl = i
        else:
            sl = i
    
print (ss,fs)
print (sl,fl)