lists = []
max_length = 0

for _ in range(5):
    new = list(input())
    lists.append(new)

    if len(new) > max_length:
        max_length = len(new)

for i in range(max_length):
    for l in lists:
        if (len(l) >= i+1):
            print(l[i], end='')