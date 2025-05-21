import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * 1001

# 점화식: dp[i] = dp[i-1] + dp[i-2]
dp[1] = 1
dp[2] = 2

for i in range(3, n+1):
    dp[i] = (dp[i-1] + dp[i-2]) % 10007

# 첫째 줄에 2×n 크기의 직사각형을 채우는 방법의 수를 10,007로 나눈 나머지를 출력한다.
print(dp[n])