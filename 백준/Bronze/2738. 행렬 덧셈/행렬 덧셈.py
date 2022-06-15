n, m = map(int, input().split())

numbers = []

for i in range(n):
    numbers.append(list(map(int, input().split())))

for i in range(n):
    numbers2 = list(map(int, input().split()))
    for j in range(m):
        numbers[i][j] += numbers2[j]

for i in range(n):
    for j in range(m):
        print(numbers[i][j], end = " ")
    print()