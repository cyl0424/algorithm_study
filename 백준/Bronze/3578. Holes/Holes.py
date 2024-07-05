n = int(input())

numbers = [0] * 4

if n == 0:
    numbers[1] += 1
else:
    while n > 0:
        if n == 1 and sum(numbers) == 0:
            numbers[0] += 1
            break
        elif n % 2 == 0:
            numbers[3] += n // 2
            break
        else:
            numbers[2] += 1
            n -= 1

res = '0'*numbers[0] + '1'*numbers[1] + '4'*numbers[2] + '8'*numbers[3]

print(res)