lists = []
max_length = 0

for _ in range(5):
    new = input()
    lists.append(new)
    if len(new) > max_length:
        max_length = len(new)

for i in range(max_length):
    for l in lists:
        if i < len(l):
            print(l[i], end='')
