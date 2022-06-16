n = int(input())

if n == 1:
    print(pow(int(input()),2))

else:
    numbers = list(map(int, input().split()))
    numbers.sort()
    print(numbers[0]*numbers[-1])