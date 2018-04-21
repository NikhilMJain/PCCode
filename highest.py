#Given an array in such a way that the elements stored in array are in increasing order initially and then after reaching to a peak element , elements stored are in decreasing order. Find the highest element.

a = [1,2,3,4,5,6,7,8,9,8,7,6,5,4,3,2,1]

l = 0 
r = len(a) - 1

while(l < r):
    if a[l] <= a[r]:
        l += 1
    else:
        r -= 1

print (a[l])
