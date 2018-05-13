a = [1,3,4,5,6,7]

a.sort()
k = 15
for i in range(len(a) - 3):
    for j in range(i + 1, len(a) - 2):
        l = j + 1
        r = len(a) - 1

        while l < r:
            if a[i] + a[j] + a[l] + a[r] == k:
                print ('{} {} {} {}'.format(a[i], a[j], a[l], a[r]))
            if a[i] + a[j] + a[l] + a[r] < k:
                l += 1
            else:
                r -= 1
