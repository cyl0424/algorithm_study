s = int(input())
m = int(input())
l = int(input())

sml = [s, m, l]
score = [1, 2, 3]

total = sum([x * y for (x, y) in zip(sml, score)])

if total >= 10:
    print('happy')
else:
    print('sad')