T = int(input())

for _ in range(T):
    case = {}
    N = int(input())

    for _ in range(N):
        S, vol = input().split()
        case[S] = int(vol)
    
    print(max(case, key=case.get))