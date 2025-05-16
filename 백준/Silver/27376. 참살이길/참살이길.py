import sys
input = sys.stdin.readline

n, k = map(int, input().split())
sign = [tuple(map(int, input().split())) for _ in range(k)]

sign.sort(key=lambda x: x[0])

current = 0
tx = 0

for x, t, s in sign:
    current += (x - tx)
    if ((current-s) // t) % 2 == 1:
        current = (((current-s) // t) + 1) * t + s
    tx = x

current += (n - tx)

print(current)