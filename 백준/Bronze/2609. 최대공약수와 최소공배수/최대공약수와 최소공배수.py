import sys

input = sys.stdin.readline

numbers = list(map(int, input().split()))
a, b = max(numbers), min(numbers)
maxN = 0
minN = 0

for i in range(1, a+1):
    if b*i < a:
        continue
    elif (b * i) % a == 0:
        minN = b*i
        break

for i in range(b, 0, -1):
    if b % i == a % i == 0:
        maxN = i
        break


print(maxN)
print(minN)