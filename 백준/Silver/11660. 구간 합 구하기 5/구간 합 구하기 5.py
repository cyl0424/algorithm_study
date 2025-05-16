import sys
input = sys.stdin.readline

n, m = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]

ps = [[0]*(n+1) for _ in range(n+1)]

for i in range(1, n+1):
    row_sum = 0
    for j in range(1, n+1):
        row_sum += A[i-1][j-1]
        ps[i][j] = ps[i-1][j] + row_sum


for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    ans = ps[x2][y2] - ps[x1-1][y2] - ps[x2][y1-1] + ps[x1-1][y1-1]
    
    print(ans)