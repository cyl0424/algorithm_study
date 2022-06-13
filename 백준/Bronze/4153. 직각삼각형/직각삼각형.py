while True:
    numbers = list(map(int, input().split()))
    numbers.sort()

    a = numbers[0]
    b = numbers[1]
    c = numbers[2]

    if a==b==c==0:
        break

    if pow(a, 2) + pow(b, 2) == pow(c, 2):
        print('right')
    else:
        print('wrong')