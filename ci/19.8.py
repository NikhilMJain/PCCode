import string
s = '''
The first question – which you should ask your interviewer – is if you’re just asking for a single word (“single query”) or if you might, eventually, use the same method for many different words (“repetitive queries”)? That is, are you simply asking for the frequency of “dog”, or might you ask for “dog,” and then “cat,” “mouse,” etc?
'''
d = {}
print(s.translate(string.punctuation).split())
for i in s.split():
    i = i.lower()
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

print(d.get('then', 'Nope'))