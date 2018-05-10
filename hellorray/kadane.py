a = [-2, -3, 4, -1, -2, 1]

def subsum():
    s = e = -1
    meh = mtn = 0
    for i in a:
        meh = meh + i
        if meh > mtn:
            mtn = meh
            e = i
        if meh < 0:
            s = i
            meh = 0
        print (meh,mtn)
        
    return mtn, (s,e)

print subsum()