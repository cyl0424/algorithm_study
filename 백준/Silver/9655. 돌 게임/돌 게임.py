import sys
input = sys.stdin.readline

n = int(input())
gamer = ["CY", "SK"]

dp = [0] * (n+1)

for i in range(1, n+1):
    dp[i] = dp[i-1] + 1
    if i >= 3:
        dp[i] = min(dp[i], dp[i-3] + 1)

print(gamer[dp[n]%2])