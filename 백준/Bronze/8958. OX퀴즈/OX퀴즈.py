n = int(input())

for _ in range(n):
    cnt = 1
    score = 0
    result = input()
    for i in result:
        if i == 'X':
            cnt = 1
        else :
            score += cnt
            cnt += 1
    print(score)         