from collections import defaultdict

N = int(input())
max_prize = 0

for _ in range(N):
    dice = list(map(int, input().split()))
    count = defaultdict(int)

    for number in dice:
        count[number] += 1

    sorted_count = sorted(count.items(), key=lambda x: (-x[1], -x[0]))

    if sorted_count[0][1] == 3:
        prize = 10000 + sorted_count[0][0] * 1000
    elif sorted_count[0][1] == 2:
        prize = 1000 + sorted_count[0][0] * 100
    else:
        prize = max(dice) * 100

    max_prize = max(max_prize, prize)

print(max_prize)
