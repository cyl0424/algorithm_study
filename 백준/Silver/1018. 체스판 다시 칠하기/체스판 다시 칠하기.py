N, M = map(int, input().split())
chess = []
res = []

for _ in range(N):
    chess.append(list(input()))

for n in range(N-7):
    for m in range(M-7):
        wStart = 0
        bStart = 0

        for i in range(n, n+8):
            for j in range(m, m+8):
                if (i+j) % 2 == 0:
                    if chess[i][j] != 'W':
                        wStart += 1
                    else:
                        bStart += 1

                else:
                    if chess[i][j] != 'B':
                        wStart += 1
                    else:
                        bStart += 1
        
        res.append(wStart)
        res.append(bStart)

print(min(res))