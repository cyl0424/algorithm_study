import sys
input = sys.stdin.readline

T = int(input())
numbers = [int(input()) for _ in range(T)]
maxNumber = max(numbers)

dp = [0] * (maxNumber+1)

dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, maxNumber+1):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

for n in numbers:
    print(dp[n])