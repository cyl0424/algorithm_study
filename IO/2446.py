# 모래시계 모양으로 별 찍기

num = int(input())

for i in range(num, 1, -1):
    print(' ' * (num - i) + '*' * (2 * i - 1))
          
for i in range(1, num + 1):
    print(' ' * (num - i) + '*' * (2 * i - 1))
