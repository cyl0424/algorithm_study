import sys
input = sys.stdin.readline

N, K = map(int, input().split())
target = tuple()
scores = []

for i in range(N):
    k, g, s, b = map(int, input().split())
    scores.append((g, s, b))

    if K == k:
        target = (g, s, b)

scores.sort(key=lambda x: (x[0], x[1], x[2]), reverse=True)

print(scores.index(target) + 1)