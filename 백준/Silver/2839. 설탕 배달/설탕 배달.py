n = int(input())
cnt = 0

while True:
    if n == 0:
        break
    elif n % 5 == 0:
        cnt += n//5
        n = 0
    elif n >= 3:
        n -= 3
        cnt += 1
    else:
        cnt = -1
        break
print(cnt)