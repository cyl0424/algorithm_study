import sys
input = sys.stdin.readline

N, K = map(int, input().split())
goods = [(0, 0)]
dp = [[0 for _ in range(K+1)] for _ in range(N+1)]

for _ in range(N):
    goods.append(tuple(map(int, input().split())))

for i in range(1, N+1):
    for j in range(1, K+1):
        w, v = goods[i][0], goods[i][1]
        
        if j < w:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w]+v)

print(dp[N][K])