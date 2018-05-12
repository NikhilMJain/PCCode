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
#abcd^e-fgh*+^*+i-
def prec(op):
    if op == '+' or op == '-':
        return 1
    elif op == '/' or op == '*':
        return 2
    elif op == '^':
        return 3
    return 0  

def itop(ex):
    for i in ex:
        if i == '(':
            s.append(i)
        elif i == ')':
            while s[-1] != '(':
                print(s.pop(),end='')
            s.pop()
        elif isOp(i):
            print('{}'.format(i),end='')
        else:
            while s and prec(i) <= prec(s[-1]):
                print('{}'.format(s.pop()),end='')
            s.append(i)
    while s:
        print('{}'.format(s.pop()),end='')

itop('a+b*(c^d-e)^(f+g*h)-i')

#ptoi('11-2/35+*')
