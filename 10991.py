# 트리모양 출력 (별 사이에 빈칸)

num = int(input())

for i in range(1, num + 1):
    print(' ' * (num - i) + '* ' * (i - 1) + '*')
