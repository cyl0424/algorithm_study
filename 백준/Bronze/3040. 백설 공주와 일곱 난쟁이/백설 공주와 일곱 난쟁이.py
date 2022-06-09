from itertools import combinations
heights=[]

for _ in range(9):
    heights.append(int(input()))

for i in combinations(heights, 7):
    if sum(i) == 100:
        right = list(i)
        for j in right:
            print(j)
        break