import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

dq = deque([i for i in range(1, N + 1)])

while len(dq) > 1:
    dq.popleft()
    dq.rotate(-1)

print(dq.pop())