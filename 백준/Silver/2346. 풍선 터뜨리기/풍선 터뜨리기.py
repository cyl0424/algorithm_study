import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
balloons = list(map(int, input().split()))

dq = deque((i + 1, balloons[i]) for i in range(N))
result = []

while dq:
    idx, move = dq.popleft()
    result.append(idx)
    if not dq:
        break

    if move > 0:
        dq.rotate(-(move - 1))
    else:
        dq.rotate(abs(move))

print(*result)