# 별 찍기 오른쪽 정렬

num = int(input())

for i in range(1, num+1):
    print(' ' * (num-i) + '*' * i)
