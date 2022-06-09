h, m = map(int, input().split())
cook = int(input())
cook_h = cook//60
cook_m = cook%60

h += cook_h
m += cook_m

if m>=60:
    m -= 60
    h += 1

if h >23:
    h -= 24

print(h, m)