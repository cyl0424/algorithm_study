n = int(input())
t = []

meeting = []
tmp = 0

for _ in range(n):
    t.append(list(map(int, input().split())))

t.sort(key=lambda x : (x[1], x[0]))

for start, end in t:
    if start >= tmp:
        tmp = end
        meeting.append([start, end])

print(len(meeting))