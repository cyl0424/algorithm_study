import sys

input = sys.stdin.readline

stair = int(input())
dp = [0] * (stair+1)
score = [0] * (stair+1)

for i in range(1, stair+1):
    score[i] = int(input())
    
if stair ==1:
    print(score[1])
    exit()
elif stair ==2:
    print(sum(score[:3]))
    exit()

dp[1] = score[1]
dp[2] = score[1] + score[2]

for i in range(3, stair+1):
    dp[i] = max(dp[i-2] + score[i], dp[i-3] + score[i-1] + score[i])

print(dp[-1])