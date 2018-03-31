for _ in range(int(raw_input().strip())):
    s = []
    p = int(raw_input().strip().split()[1])
    for i in raw_input().strip().split():
        if p % int(i) == 0 and p / int(i) in s:
            print('Yes')
            break
        s.append(int(i))
    else:
        print('No')