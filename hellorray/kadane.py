a = [1,4,3,2,-2,3,-4,3,-2,-5,8,7]

def subsum():
    meh = mtn = 0
    for i in a:
        meh = meh + i
        if meh > mtn:
            mtn = meh
        if meh < 0:
            meh = 0
    return mtn

print subsum()