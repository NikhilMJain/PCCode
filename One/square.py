class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def d(P1, P2):
    return (((P2.x - P1.x) ** 2) + ((P2.y - P1.y) ** 2)) ** (1 / 2)

def sd(P1, P2):
    return (((P2.x - P1.x) ** 2) + ((P2.y - P1.y) ** 2))

A = Point(10, 30)
B = Point(20, 20)
C = Point(20, 10)
D = Point(10, 40)

if (sd(A, C) == sd(A, B) + sd(B, C) and d(C, D) == d(B, C)) or \
    (sd(B, D) == sd(B, C) + sd(C, D) and d(D, A) == d(C, D)) or \
    (sd(C, A) == sd(C, D) + sd(D, A) and d(A, B) == d(D, A)) or \
    (sd(D, B) == sd(D, A) + sd(A, B) and d(B, C) == d(A, B)):
    print True
else:
    print False