n = int(input())
max_prize = 0

for _ in range(n):
    res = 0
    a, b, c = map(int, input().split())
    
    if (a == b == c):
        res = 10000 + (a * 1000)
    elif (a == b or b == c):
        res = 1000 + (b * 100)
    elif (c == a):
        res = 1000 + (a * 100)
    else:
        res = max(a, b, c) * 100
    
    if max_prize < res:
        max_prize = res

print(max_prize)