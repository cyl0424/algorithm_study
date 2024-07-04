N, K = map(int, input().split())

raw = list(range(1, N + 1))
res = []

idx = 0

for _ in range(N):
    idx = (idx + K - 1) % len(raw)
    res.append(raw.pop(idx))

res_num = ', '.join(str(a) for a in res)
print(f'<{res_num}>')