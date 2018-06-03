for _ in range(int(raw_input().strip())):
    l = [int(i) for i in raw_input().strip().split()]
    d = {}
    for i in l:
        if i in d:
            d[-i] = True
        else:
            d[i] = False
    for i in d:
        if d[i]:
            print(i, -i,)