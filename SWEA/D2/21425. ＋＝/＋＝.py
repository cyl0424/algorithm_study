T = int(input())

for test_case in range(1, T + 1):
    a, b, N = map(int, input().split())
    res = 0

    while max(a, b) <= N:
        if a < b:
            a += b
        else:
            b += a
        res += 1

    print(res)