T = int(input())

for i in range(T):
    whole = int(input())
    q = 0
    d = 0
    n = 0
    p = 0

    while whole > 0:
        if whole >= 25:
            q += 1
            whole -= 25
        elif whole >= 10:
            d += 1
            whole -= 10
        elif whole >= 5:
            n += 1
            whole -= 5
        else:
            p += whole
            whole = 0
        
    print(q, d, n, p)