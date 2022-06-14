T = int(input())

for _ in range(T):
    floor = int(input())
    num = int(input())
    numbers = list(range(1, num+1))
    for i in range(floor):
        for j in range(1, num):
            numbers[j] += numbers[j-1]
    print(numbers[-1])

