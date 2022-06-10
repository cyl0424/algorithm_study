num, height = map(int, input().split())
hole = list(map(int, input().split()))
hole.sort()

current = hole[0]
result = 1

for i in hole:
    if current+height <= i:
        current = i
        result += 1

print(result)
