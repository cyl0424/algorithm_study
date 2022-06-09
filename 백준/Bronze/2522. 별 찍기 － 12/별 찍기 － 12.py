num = int(input())

for i in range(1, num+1):
    print(' ' * (num-i) + '*' * i)

for j in range(1, num):
    print(' ' * j + '*' * (num-j))
    