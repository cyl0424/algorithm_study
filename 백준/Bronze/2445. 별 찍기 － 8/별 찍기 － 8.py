num = int(input())

for i in range(1, num):
    print('*' * i, end = '')
    print(' ' * (2 * (num -i)), end = '')
    print('*' * i)

for j in range(num, 0, -1):
    print('*' * j, end = '')
    print(' ' * (2 * (num -j)), end = '')
    print('*' * j)