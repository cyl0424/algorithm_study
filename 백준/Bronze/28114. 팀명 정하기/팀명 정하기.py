import sys
input = sys.stdin.readline

entries = []
for _ in range(3):
    score, year, name = input().split()
    entries.append((int(score), int(year) % 100, name))

std_nums = sorted(str(y) for _, y, _ in entries)
print(''.join(std_nums))

initials = ''.join(name[0] for score, _, name in sorted(entries, key=lambda x: x[0], reverse=True))
print(initials)