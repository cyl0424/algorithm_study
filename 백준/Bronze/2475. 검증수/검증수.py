total = 0
numbers = list(map(int, input().split()))

for i in numbers:
    total += i*i

print(total%10)