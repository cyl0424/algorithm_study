import sys
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    K = int(input())
    files = [0] + list(map(int, input().split()))

    prefix = [0] * (K+1)

    for i in range(1, K+1):
        prefix[i] = prefix[i-1] + files[i]

    dp = [[0] * (K+1) for _ in range(K+1)]

    # cnt = 합쳐질 파일의 개수
    for cnt in range(2, K+1):
        for start in range(1, K - cnt + 2):
            end = start + cnt-1

            dp[start][end] = sys.maxsize

            for mid in range(start, end):
                # 기존 계산 값과, 새로운 계산 값 (start~mid, mid+1~end 까지 합친 뒤 start~end로 합치기) 비교
                dp[start][end] = min(dp[start][end],
                                     dp[start][mid] + dp[mid+1][end])
            
            dp[start][end] += prefix[end] - prefix[start-1]

    print(dp[1][K])