# 오른쪽 정렬 증감 별찍기

num = int(input())

for i in range(1, num):
    print(' ' * (num-i) + '*' * i)

for i in range(num, 0, -1):
    print(' ' * (num-i) + '*' * i)
