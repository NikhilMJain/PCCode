def m():
    print(m.x,m.y)
    m.x = 14
    m.y = 15

    pass

m.x = 4
m.y = 5

m()

print(m.x,m.y)

m()