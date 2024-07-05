a, b = map(int, input().split())

cnt = 0

while a < b:
    if b % 2 == 0:
        cnt += 1
        b //= 2
    elif list(str(b))[-1] == '1':
        cnt += 1
        b //= 10
    else:
        break


if a == b:
    print(cnt+1)
else:
    print(-1)