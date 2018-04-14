a = [100, 180, 260, 310, 40, 535, 695]
l = len(a)
i = 0

while i < l - 1:
    while i < l - 1 and a[i] > a[i+1]:
        i += 1
    print('buy {}'.format(a[i]))
    i += 1
    while i < l - 1 and a[i] < a[i + 1]:
        i+=1
    print('sell {}'.format(a[i]))
    i+=1
