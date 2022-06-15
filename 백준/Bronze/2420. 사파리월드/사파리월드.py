numbers = list(map(int, input().split()))
numbers.sort()
print(abs(numbers[1]-numbers[0]))