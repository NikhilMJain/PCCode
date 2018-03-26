a = [1,2,3,4,5,6,7,8,9]
l = 0
h = len(a) - 1
key = 9
while(l <= h):
    mid = (l + h) // 2
    if key == a[mid]:
        print mid
        exit()
    elif key < a[mid]:
        h = h-1
    else:
        l = l + 1
print 'not found'

