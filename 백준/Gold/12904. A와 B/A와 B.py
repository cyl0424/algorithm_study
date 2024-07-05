s = list(input().rstrip())
t = list(input().rstrip())

while len(t) >= len(s):
    if t[-1] == 'A':
        t.pop()
    elif t[-1] == 'B':
        t.pop()
        t.reverse()
    
    if s == t:
        print(1)
    elif len(t) == len(s):
        print(0)