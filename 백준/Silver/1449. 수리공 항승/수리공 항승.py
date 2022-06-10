num, height = map(int, input().split())
hole = [False]*1001

for i in map(int, input().split()):
    hole[i] = True

current = 0
result = 0

while current < 1001:
    if hole[current]:
        current += height
        result += 1
    else:
        current += 1

print(result)