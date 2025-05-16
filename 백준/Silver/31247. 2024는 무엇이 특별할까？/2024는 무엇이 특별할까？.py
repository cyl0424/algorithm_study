import sys
input=sys.stdin.readline

T = int(input())
out = []

for _ in range(T):
    N, K=map(int,input().split())
    if K >= 61:
        out.append("0")
    else:
        d1 = 1<<K
        d2 = d1<<1
        out.append(str(N//d1 - N//d2))

print("\n".join(out))