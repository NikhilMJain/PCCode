s = []
l = ['+','-','/','*','^']

def isOp(op):
    return op not in l

def ptoi(ex):
    for i in ex:
        if isOp(i):
            s.append(i)
        else:
            b = s.pop()
            a = s.pop()
            s.append('({}{}{})'.format(a,i,b))
    print(s.pop())

#ptoi('abcd-*e/+')

def prec(op):
    if op == '+' or op == '-':
        return 1
    elif op == '/' or op == '*':
        return 2
    elif op == '^':
        return 3    

def itop(ex):
    for i in ex:
        if i == '(':
            s.append(i)
        elif i == ')':
            while s[-1] != '(':
                print(s.pop())
            s.pop()
        elif isOp(i):
            print('{}'.format(i))
        else:
            while s and prec(i) <= prec(s[-1]):
                print(''.format(s.pop()))
            s.append(i)
    while s:
        print('{}'.format(s.pop()))

itop('a+(b*c)')
