num = int(input())
coordinate = []

for _ in range(num):
    coordinate.append(tuple(map(int, input().split())))

coordinate.sort(key=lambda x : x[1])
coordinate.sort(key=lambda x : x[0])

for i in coordinate:
    print(i[0], i[1])
