n = int(input())
ropes = []
max_list = []

for _ in range(n):
    ropes.append(int(input()))

ropes.sort()

for i in range(len(ropes)):
    cnt = len(ropes) - i
    weight = ropes[i] * cnt

    max_list.append(weight)

print(max(max_list))