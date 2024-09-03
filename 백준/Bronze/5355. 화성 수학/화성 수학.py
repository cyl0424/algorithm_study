T = int(input())

for _ in range(T):
    case = input().split()
    n = float(case[0])
    case = case[1:]
    
    for o in case:
        if o == '@':
            n *= 3
            
        elif o == '%':
            n += 5
            
        elif o == '#':
            n -= 7
            
    print(f'{n:.2f}')
