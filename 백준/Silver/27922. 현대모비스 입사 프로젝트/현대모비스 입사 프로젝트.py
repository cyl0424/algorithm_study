import sys
input = sys.stdin.readline

N, K = map(int, input().split())
sum_ab = [0] * N
sum_ac = [0] * N
sum_bc = [0] * N

for i in range(N):
    a, b, c = map(int, input().split())
    sum_ab[i] = a + b
    sum_ac[i] = a + c
    sum_bc[i] = b + c

sum_ab.sort(reverse=True)
sum_ac.sort(reverse=True)
sum_bc.sort(reverse=True)

result = max(
    sum(sum_ab[:K]),
    sum(sum_ac[:K]),
    sum(sum_bc[:K])
)

print(result)