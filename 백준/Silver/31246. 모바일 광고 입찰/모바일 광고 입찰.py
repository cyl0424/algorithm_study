import sys
input = sys.stdin.readline

N, K = map(int, input().split())
diff = []

for _ in range(N):
    a, b = map(int, input().split())
    diff.append(a-b)

diff.sort(reverse=True)
res = 0

if diff[K-1] < 0:
    res = diff[K-1] * (-1)

print(res)