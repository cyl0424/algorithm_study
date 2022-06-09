x = int(input())

for i in range(x):
    a, b = map(int, input().split())
    print(f'Case #{i+1}: {a+b}')