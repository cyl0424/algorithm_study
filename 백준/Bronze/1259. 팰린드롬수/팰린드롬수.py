while True:
    number = input()

    if number == '0':
        break
    else:
        number = list(number)

    if len(number) % 2 ==0:
        half = len(number)//2
    else:
        half = len(number)// 2

    if number[:half] == number[-1:-half-1:-1]:
        print('yes')
    else:
        print('no')