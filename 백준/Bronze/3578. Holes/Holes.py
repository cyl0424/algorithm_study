n = int(input())

res = ''

if n == 0:
    res = '1'
elif n == 1:
    res = '0'
else:
    if n % 2 == 0:
        res = '8' * (n//2)
    else:
        res = '4' + '8' * (n//2)

print(res)