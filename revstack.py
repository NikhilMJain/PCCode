s = [1,2,3,4]

def rev():
    if s:
        t = s.pop()
        rev()
        insert(t)

def insert(item):
    if not s:
        s.append(item)
    else:
        temp = s.pop()
        insert(item)
        s.append(temp)
        
print(s)
rev()
print(s)